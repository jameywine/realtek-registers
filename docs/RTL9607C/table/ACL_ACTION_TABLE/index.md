---
tags:
  - RTL9607C
  - Table
  - Table Fields
---

# RTL9607C table: ACL_ACTION_TABLE

## Details

*Name* ACL_ACTION_TABLE

*Feature* [TABLE_ACCESS](../../feature/TABLE_ACCESS)

*Type* 3

*Entries* 128

*Control register* [TBL_ACCESS_CTRL](../../register/TBL_ACCESS_CTRL)

*Write Data register* [TBL_ACCESS_WR_DATA](../../register/TBL_ACCESS_WR_DATA)

*Read Data register* [TBL_ACCESS_RR_DATA](../../register/TBL_ACCESS_RR_DATA)

## Description

## Fields

|Name|LSB|Bits|Description|
| :--- | :--- | :--- | :--- |
|HIT|63|1||
|ACLINT|62|1||
|PRIACT|59|3||
|PRIDX|51|8||
|FWDACT|49|2||
|FWD_PMSK|38|11||
|POLICACT|36|2||
|METER_IDX|30|6||
|SACT|27|3||
|SVID|15|12||
|CACT|12|3||
|CVID|0|12||
