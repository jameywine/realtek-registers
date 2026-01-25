import pandas as pd
from mdutils.mdutils import MdUtils
from itertools import chain
import os

# Helper to format bit ranges
def format_bits(lsp: int, length: int) -> str:
	msb = lsp + length - 1
	return f"{msb}:{lsp}" if msb != lsp else str(msb)

def sort_by_hex(s: pd.Series) -> pd.Series:
	s_no_prefix = s.str.replace(r"^0x", "", case=False, regex=True)
	return pd.to_numeric(s_no_prefix.apply(lambda x: int(x, 16)), errors="coerce")

# TODO: get the name from argument
chip_name = "RTL9607C"
os.makedirs(chip_name, exist_ok = True)
mdfile_name = "index.md"

table_access_regs = {
	'TBL_ACCESS_CTRL' : {
		"Name" : ["L2_MC_DSL", "L2_UC", "L3_MC", "L3_MC_FID", "L3_MC_VID", "VLAN", "ACL_DATA", "ACL_MASK", "ACL_ACTION_TABLE", "CF_MASK_T0", "CF_MASK_T1", "CF_MASK_T2", "CF_RULE_T0", "CF_RULE_T1", "CF_RULE_T2", "CF_ACTION_DS", "CF_ACTION_US"],
		"Type" : [0, 0, 0, 0, 0, 1, 2, 2, 3, 4, 4, 4, 4, 4, 4, 5, 5],
		"Size": [2112, 2112, 2112, 2112, 2112, 4096, 128, 128, 128, 256, 256, 256, 256, 256, 256, 256, 256],
		"WD_DATA": "TBL_ACCESS_WR_DATA",
		"RD_DATA": "TBL_ACCESS_RR_DATA"
		},
	'NAT_TBL_ACCESS_CTRL' : {
		"Name": [ "INTERFACE", "ETHER_TYPE", "CAM_TAG", "FB_EXT_PORT", "WAN_ACCESS_LIMIT", "FLOW_TABLE_PATH1_2", "FLOW_TABLE_PATH3_4", "FLOW_TABLE_PATH5", "FLOW_TABLE_PATH6", "CAM", "MAC_IDX", "FLOW_TABLE_TAG", "TCAM", "TCAM_RAW_TABLE_PATH1_2", "TCAM_RAW_TABLE_PATH3_5"],
		"Type": [0, 1, 2, 3, 4, 8, 8, 8, 8, 8, 9, 10, 11, 12, 13, 13],
		"Size": [16, 8, 64, 32, 32, 4096, 4096, 4096, 4096, 64, 256, 4096, 64, 64, 64],
		"WD_DATA": "NAT_TBL_ACCESS_WR_DATA",
		"RD_DATA": "NAT_TBL_ACCESS_RR_DATA"
		}
}

register_tables_header = ["Name", "Type", "Summary"]

# Load CSVs
reg_df = pd.read_csv("reglist-rtl9607c.csv", header=None, names=["Feature", "Register", "Offset", "Fields", "Bit Offset", "Array Range", "Port Range"])
field_df = pd.read_csv("regfieldlist-rtl9607c.csv", header=None, names=["Feature", "Register", "Field", "LSP", "Length"])

# For lookups later
fields_by_reg = { name: grp for name, grp in field_df.groupby("Register", sort=False)}

# Makedown file for a unified Feature list
mdfile_features = MdUtils(file_name=f"./{chip_name}/feature/" + mdfile_name)
mdfile_features.write(f"---\ntags:\n  - {chip_name}\n  - Feature List\n---\n\n")
mdfile_features.write(f"# {chip_name} Features\n\n")

# Define the variables for feature table in Makedown
features_header = ["Name", "Registers"]
features_names = []
registers_num = []

# Sort the csv file by Offset with the help of the key function
regs_df_sorted = reg_df.sort_values(by="Offset", key=sort_by_hex)

# Group them by Feature for later iteration
regs_by_feature = regs_df_sorted.groupby("Feature", sort=False)

# Makedown file for a unified Register list
mdfile_registers = MdUtils(file_name=f"./{chip_name}/" + mdfile_name)
mdfile_registers.write(f"---\ntags:\n  - {chip_name}\n  - Register List\n---\n\n")
mdfile_registers.write(f"# {chip_name} Registers\n")

priv_feature = ""

# Iterate through the registers to fill out the unified register markdown file
for group_registers in regs_df_sorted.itertuples():
	feature = group_registers.Feature
	register = group_registers.Register
	offset = group_registers.Offset
	if priv_feature != feature:
		mdfile_registers.write(f"\n## [{feature}](feature/{feature})\n")
		priv_feature = feature
		mdfile_registers.write("\n|Offset|Name|Summary|\n")
		mdfile_registers.write("| :--- | :--- | :--- |\n")
	mdfile_registers.write(f"|{offset}|[{register}](register/{register})||\n")

mdfile_registers.create_md_file()

# Iterate through the registers by Feature groups to fill out "seperated" register and feature markdown files

for feature, group in regs_df_sorted.groupby("Feature", sort=False):

	feature_dir = f"./{chip_name}/feature/{feature}/"
	os.makedirs(feature_dir, exist_ok = True)

	# Makedown file for a single feature file
	mdfile_feature = MdUtils(file_name=feature_dir + mdfile_name)
	mdfile_feature.write(f"---\ntags:\n  - {chip_name}\n  - Feature\n  - Register List\n---\n\n")
	mdfile_feature.write(f"# {chip_name} Feature: {feature}\n\n")

	feature_header = ["Offset", "Name", "Description"]
	offsets = group["Offset"].tolist()
	register_names = group["Register"].apply(lambda reg: f"[{reg}](../../register/{reg})").tolist()
	descriptions = [""] * group.shape[0]
	rows = list(zip(offsets, register_names, descriptions))
	list_of_regs = list(chain(feature_header, *rows))

	mdfile_feature.new_table(columns=3, rows=group.shape[0]+1, text=list_of_regs, text_align='left')
	mdfile_feature.create_md_file()

	# Append the name of Feature and its number of register to the unified features file
	features_names.append(f"[{feature}]({feature})")
	registers_num.append(f"{group.shape[0]}")

	# Iterate through the rows of the Feature group to fill single register file
	for _, row in group.iterrows():

		register_name = row["Register"]
		register_dir = f"./{chip_name}/register/{register_name}/"
		os.makedirs(register_dir, exist_ok = True)

		mdfile_register = MdUtils(file_name=register_dir + mdfile_name)
		mdfile_register.write(f"---\ntags:\n  - {chip_name}\n  - Register\n  - Register Fields\n---\n\n")
		mdfile_register.write(f"# {chip_name} register: {register_name}\n\n")
		mdfile_register.write(f"## Details\n\n")
		mdfile_register.write(f"*Name* {register_name}\n\n")
		mdfile_register.write(f"*Offset* {row["Offset"]}\n\n")
		mdfile_register.write(f"*Feature* [{feature}](../../feature/{feature})\n\n")

		if row["Bit Offset"] != 0:
			mdfile_register.write(f"*Bit Offset:* {row['Bit Offset']}\n\n")
		if row["Array Range"] != "0-0":
			mdfile_register.write(f"*Array Range:* {row['Array Range']}\n\n")
		if row["Port Range"] != "0-0":
			mdfile_register.write(f"*Port Range:* {row['Port Range']}\n\n")

		grouplist = fields_by_reg[register_name]

		mdfile_register.write("## Description\n\n")
		mdfile_register.write("## Fields\n\n")

		bits_header = ["Bit(s)", "Field Name", "Description"]
		bits = [format_bits(lsb, length) for lsb, length in zip(grouplist["LSP"], grouplist["Length"])]
		field_names = grouplist["Field"].tolist()
		bits_descriptions = [""] * len(grouplist)
		bit_rows = list(zip(bits, field_names, bits_descriptions))
		list_of_fields = list(chain(bits_header, *bit_rows))

		mdfile_register.new_table(columns=3, rows=grouplist.shape[0]+1, text = list_of_fields, text_align='left')

		if register_name in table_access_regs:
			mdfile_register.write("\n## Control tables\n\n")
			register_tables_name = table_access_regs[register_name]['Name']
			register_tables_type = table_access_regs[register_name]['Type']
			register_tables_row_num = len(register_tables_name)
			register_tables_summary = [""] * register_tables_row_num
			register_tables_rows = list(zip(register_tables_name, register_tables_type, register_tables_summary))
			list_of_register_tables = list(chain(register_tables_header, *register_tables_rows))
			mdfile_register.new_table(columns=3, rows=register_tables_row_num+1, text=list_of_register_tables, text_align='left')

		mdfile_register.create_md_file()

features_rows = list(zip(features_names, registers_num))
list_of_features = list(chain(features_header, *features_rows))

mdfile_features.new_table(columns=2, rows=regs_by_feature.ngroups+1, text=list_of_features, text_align='left')
mdfile_features.create_md_file()

# Create CPU Tags

cputags_df = pd.read_csv("cputag-rtl9607c.csv", header=None, names=["Direction", "Name", "LSB", "Bits"])

previous_tag = ""
os.makedirs(f"./{chip_name}/cputag/", exist_ok = True)

# Markdown file for CPU Tags
mdfile_cputags = MdUtils(file_name=f"./{chip_name}/cputag/" + mdfile_name)
mdfile_cputags.write(f"---\ntags:\n  - {chip_name}\n  - CPU Tags\n---\n\n")
mdfile_cputags.write(f"# {chip_name} CPU tags\n")

for group_tags in cputags_df.itertuples():
	direction = group_tags.Direction

	if previous_tag != direction:
		mdfile_cputags.write(f"\n## Frame direction:  {direction.upper()}\n")
		mdfile_cputags.write("\n|Name|LSB|Bits|Description|\n")
		mdfile_cputags.write("| :--- | :--- | :--- | :--- |\n")
		previous_tag = direction

	mdfile_cputags.write(f"|{group_tags.Name}|{group_tags.LSB}|{group_tags.Bits}||\n")

mdfile_cputags.create_md_file()

# Create Table Markdown & Individual Tables Markdowns
mdfile_tables = MdUtils(file_name=f"./{chip_name}/table/" + mdfile_name)
mdfile_tables.write(f"---\ntags:\n  - {chip_name}\n  - Table List\n---\n\n")
mdfile_tables.write(f"# {chip_name} tables\n")
table_header = ["Name", "Size", "Type", "Summary"]

tablefield_df = pd.read_csv("tablefieldlist-rtl9607c.csv", header=None, names=["Feature", "Table", "Field", "LSB", "Bits"])
fields_by_table = { name: grp for name, grp in tablefield_df.groupby("Table", sort=False)}
os.makedirs(f"./{chip_name}/table/", exist_ok = True)

for table_name in table_access_regs:
	mdfile_tables.write(f"\n## [{table_name}](../register/{table_name})\n")
	table_row_num = len(table_access_regs[table_name]['Name'])
	table_names = table_access_regs[table_name]['Name']
	table_names = list(map(lambda t: f"[{t}]({t})", table_names))
	table_type = table_access_regs[table_name]['Type']
	table_size = table_access_regs[table_name]['Size']
	table_summary = [""] * table_row_num
	table_rows = list(zip(table_names, table_size, table_type, table_summary))
	table_list = list(chain(table_header, *table_rows))
	mdfile_tables.new_table(columns = len(table_header), rows = table_row_num + 1, text = table_list, text_align='left')
	table_wd_data = table_access_regs[table_name]["WD_DATA"]
	table_rd_data = table_access_regs[table_name]["RD_DATA"]

	for index, table in enumerate(table_access_regs[table_name]['Name']):

		table_dir = f"./{chip_name}/table/{table}/"
		os.makedirs(table_dir, exist_ok = True)
		mdfile_table = MdUtils(file_name=table_dir + mdfile_name)
		mdfile_table.write(f"---\ntags:\n  - {chip_name}\n  - Table\n  - Table Fields\n---\n\n")
		mdfile_table.write(f"# {chip_name} table: {table}\n")
		mdfile_table.write(f"\n## Details\n")
		mdfile_table.write(f"\n*Name* {table}\n")
		mdfile_table.write(f"\n*Feature* [TABLE_ACCESS](../../feature/TABLE_ACCESS)\n")
		mdfile_table.write(f"\n*Type* {table_type[index]}\n")
		mdfile_table.write(f"\n*Entries* {table_size[index]}\n")
		mdfile_table.write(f"\n*Control register* [{table_name}](../../register/{table_name})\n")
		mdfile_table.write(f"\n*Write Data register* [{table_wd_data}](../../register/{table_wd_data})\n")
		mdfile_table.write(f"\n*Read Data register* [{table_rd_data}](../../register/{table_rd_data})\n")
		mdfile_table.write(f"\n## Description\n")
		mdfile_table.write(f"\n## Fields\n")

		table_fields_group = fields_by_table[table]
		table_fields_header = ["Name", "LSB", "Bits", "Description"]
		table_fields_name = table_fields_group["Field"]
		table_fields_lsb = table_fields_group["LSB"]
		table_fields_bits = table_fields_group["Bits"]
		table_fields_descriptions = [""] * len(table_fields_group)
		table_fields_rows = list(zip(table_fields_name, table_fields_lsb, table_fields_bits, table_fields_descriptions))
		table_fields_list = list(chain(table_fields_header, *table_fields_rows))
		mdfile_table.new_table(columns = len(table_fields_header), rows = table_fields_group.shape[0] + 1, text = table_fields_list, text_align='left')
		mdfile_table.create_md_file()

mdfile_tables.create_md_file()
