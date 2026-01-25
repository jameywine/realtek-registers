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

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:26|RESERVED||
|25|RD_EXE||
|24|WR_EXE||
|23:20|RESERVED||
|19:16|TBL_IDX||
|15:0|ETRY_IDX||

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
