---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: NAT_TBL_ACCESS_CTRL

## Details

*Name* NAT_TBL_ACCESS_CTRL

*Offset* 0x801100

*Feature* [TABLE_ACCESS](../../feature/TABLE_ACCESS)

## Description

NAT Table Access control register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:26|RESERVED||
|25|RD_EXE|Trigger hardware to execute read indirect table access. Also means status.<br>0b0: completed<br>0b1: executing<br>(Note: this bit is common used by software and hardware. When hardware completes the table access, it will clear this bit. File it with 1 to perform command. )|
|24|WR_EXE|Trigger hardware to execute write indirect table access. Also means status.<br>0b0: completed<br>0b1: executing<br>(Note: this bit is common used by software and hardware. When hardware completes the table access, it will clear this bit. File it with 1 to perform command. )|
|23:20|RESERVED||
|19:16|TBL_IDX|Access table type.<br>4’d0(4’b0000): interface table<br>4’d1(4’b0001): ether_type table<br>4’d2(4’b0010): cam_tag table<br>4’d3(4’b0011): fb_ext_port table<br>4’d4(4’b0100): wan_access_limit table<br>4’d8(4’b1000): flow_table_path/cam table<br>4’d9(4’b1001): mac_idx table<br>4’d10(4’b1010): flow_table_tag table<br>4’d10(4’b1011): tcam table<br>4’d10(4’b1100): tcam_raw_table_path1_2 table<br>4’d10(4’b1101): tcam_raw_table_path3_5 table<br>Others: RESERVED|
|15:0|ETRY_IDX|Select access address of the table. Can't be bigger than the number of entries in the table being accessed.|

## Control tables


|Name|Type|Summary|
| :--- | :--- | :--- |
|INTERFACE|0||
|ETHER_TYPE|1||
|CAM_TAG|2||
|FB_EXT_PORT|3||
|WAN_ACCESS_LIMIT|4||
|FLOW_TABLE_PATH1_2|8||
|FLOW_TABLE_PATH3_4|8||
|FLOW_TABLE_PATH5|8||
|FLOW_TABLE_PATH6|8||
|CAM|8||
|MAC_IDX|9||
|FLOW_TABLE_TAG|10||
|TCAM|11||
|TCAM_RAW_TABLE_PATH1_2|12||
|TCAM_RAW_TABLE_PATH3_5|13||
