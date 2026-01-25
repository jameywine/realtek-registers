---
tags:
  - RTL9607C
  - Table
  - Table Fields
---

# RTL9607C table: TCAM_RAW_TABLE_PATH1_2

## Details

*Name* TCAM_RAW_TABLE_PATH1_2

*Feature* [TABLE_ACCESS](../../feature/TABLE_ACCESS)

*Type* 12

*Entries* 64

*Control register* [NAT_TBL_ACCESS_CTRL](../../register/NAT_TBL_ACCESS_CTRL)

*Write Data register* [NAT_TBL_ACCESS_WR_DATA](../../register/NAT_TBL_ACCESS_WR_DATA)

*Read Data register* [NAT_TBL_ACCESS_RR_DATA](../../register/NAT_TBL_ACCESS_RR_DATA)

## Description

## Fields

|Name|LSB|Bits|Description|
| :--- | :--- | :--- | :--- |
|VALID|144|1||
|I_CPRI|135|3||
|L2_PTC|92|7||
|EXT_SPA|89|3||
|SPA|85|4||
|SVLAN|73|12||
|CVLAN|61|12||
|DA_IDX|49|12||
|SA_IDX|37|12||
|PPP_ID|21|16||
|TOS|13|8||
|I_PPPOE_IF|12|1||
|STAG_IF|11|1||
|CTAG_IF|10|1||
|MACT|9|1||
|STM_IDX|2|7||
|PTH|0|2||
