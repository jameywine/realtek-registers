---
tags:
  - RTL9607C
  - Table
  - Table Fields
---

# RTL9607C table: CF_ACTION_US

## Details

*Name* CF_ACTION_US

*Feature* [TABLE_ACCESS](../../feature/TABLE_ACCESS)

*Type* 5

*Entries* 256

*Control register* [TBL_ACCESS_CTRL](../../register/TBL_ACCESS_CTRL)

*Write Data register* [TBL_ACCESS_WR_DATA](../../register/TBL_ACCESS_WR_DATA)

*Read Data register* [TBL_ACCESS_RR_DATA](../../register/TBL_ACCESS_RR_DATA)

## Description

Classification upstrean action control table

## Fields

|Name|LSB|Bits|Description|
| :--- | :--- | :--- | :--- |
|CPRI_ACT|57|3|Assigned classification priority action|
|CVID_ACT|54|3|Assigned C tag VID action|
|C_PRI|51|3|Assigned C tag P-bits|
|C_VID|39|12|Assigned C tag VID|
|CACT|37|2|0b00:nop<br>0b01:un-tagging<br>0b10:Translation with C2S table<br>0b11:Transparent(ingnore VLAN egress filtering and keep egress C-tag format)|
|DROP_TRAP_ACT|35|2|Drop Trap Action?|
|ASSIGN_IDX|28|7|Assigned PON MAC stream ID or QID|
|SID_ACT|23|1|0b0:Assign to SID<br>0b1:Assign to QID|
|CSVID_ACT|21|2|0b00:Assigned to VID<br>0b01:Copy from 1st tag VID (if 1st tag is not existed, then using CS_VID)<br>0b10:Copy from 2nd tag VID (if 2nd tag is not existed, then using CS_VID)<br>Other:reserved|
|CSPRI_ACT|18|3|Assigned Stag P-bits Action|
|CS_PRI|15|3|Assigned Stag P-bits|
|CS_VID|3|12|Assigned Stag VID|
|CSACT|0|3|0b000:nop (follow switch-core)<br>0b001:add classification tag which TPID as VS_TPID (reference to CSVID_ACT/CSPRI_ACT)<br>0b010:add classification tag which TPID as 0x8100 (reference to CSVID_ACT/CSPRI_ACT)<br>0b011:delete Stag<br>0b100: transparent<br>Other: reserved|
