---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: TBL_ACCESS_CTRL

## Details

*Name* TBL_ACCESS_CTRL

*Offset* 0x12000

*Feature* [TABLE_ACCESS](../../feature/TABLE_ACCESS)

## Description

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31|ACS_CMD_PS||
|30:24|RESERVED||
|23:12|ADDR||
|11:8|SPA||
|7:5|ACCESS_METHOD||
|4:3|CMD_TYPE||
|2:0|TBL_TYPE||

## Control tables


|Name|Type|Summary|
| :--- | :--- | :--- |
|L2_MC_DSL|0||
|L2_UC|0||
|L3_MC|0||
|L3_MC_FID|0||
|L3_MC_VID|0||
|VLAN|1||
|ACL_DATA|2||
|ACL_MASK|2||
|ACL_ACTION_TABLE|3||
|CF_MASK_T0|4||
|CF_MASK_T1|4||
|CF_MASK_T2|4||
|CF_RULE_T0|4||
|CF_RULE_T1|4||
|CF_RULE_T2|4||
|CF_ACTION_DS|5||
|CF_ACTION_US|5||
