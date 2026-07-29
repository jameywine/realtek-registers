---
tags:
  - RTL9607C
  - Table
  - Table Fields
---

# RTL9607C table: CF_MASK_T2

## Details

*Name* CF_MASK_T2

*Feature* [TABLE_ACCESS](../../feature/TABLE_ACCESS)

*Type* 4

*Entries* 256

*Control register* [TBL_ACCESS_CTRL](../../register/TBL_ACCESS_CTRL)

*Write Data register* [TBL_ACCESS_WR_DATA](../../register/TBL_ACCESS_WR_DATA)

*Read Data register* [TBL_ACCESS_RR_DATA](../../register/TBL_ACCESS_RR_DATA)

## Description

Classification rule mask table 2

## Fields

|Name|LSB|Bits|Description|
| :--- | :--- | :--- | :--- |
|VALID|48|1|valid bit|
|CTAG|32|16||
|U_D|31|1|Rule of upstream or downstream<br>0b0:upstream<br>0b1:downstream|
|TOS_GEMIDX|23|8|Upstream TOS or downstream GEMIDX or LLID|
|OUTER_TAG|7|16||
|STPID|6|1||
|IF_STAG|5|1|has S-tag|
|IF_CTAG|4|1|has C-tag|
|UNI|0|4|UNI/UTP port|
