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

# Load CSVs
reg_df = pd.read_csv("reglist-rtl9607c.csv", header=None, names=["Feature", "Register", "Offset", "Fields", "Bit Offset", "Array Range", "Port Range"])
field_df = pd.read_csv("regfieldlist-rtl9607c.csv", header=None, names=["Feature", "Register", "Field", "LSP", "Length"])

# For lookups later
fields_by_reg = { name: grp for name, grp in field_df.groupby("Register", sort=False)}

# Makedown file for a unified Feature list
mdfile_features = MdUtils(file_name=f"./{chip_name}/feature/" + mdfile_name)
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
		mdfile_register.write(f"# {register_name} Details\n\n")
		mdfile_register.write(f"*Offset:* {row["Offset"]}\n\n")
		mdfile_register.write(f"*Feature:* [{feature}](../../feature/{feature})\n\n")

		if row["Bit Offset"] != 0:
			mdfile_register.write(f"*Bit Offset:* {row['Bit Offset']}\n\n")
		if row["Array Range"] != "0-0":
			mdfile_register.write(f"*Array Range:* {row['Array Range']}\n\n")
		if row["Port Range"] != "0-0":
			mdfile_register.write(f"*Port Range:* {row['Port Range']}\n\n")

		grouplist = fields_by_reg[register_name]

		mdfile_register.write("## Fields\n\n")

		bits_header = ["Bit(s)", "Field Name", "Description"]
		bits = [format_bits(lsb, length) for lsb, length in zip(grouplist["LSP"], grouplist["Length"])]
		field_names = grouplist["Field"].tolist()
		bits_descriptions = [""] * len(grouplist)
		bit_rows = list(zip(bits, field_names, bits_descriptions))
		list_of_fields = list(chain(bits_header, *bit_rows))

		mdfile_register.new_table(columns=3, rows=grouplist.shape[0]+1, text = list_of_fields, text_align='left')
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
