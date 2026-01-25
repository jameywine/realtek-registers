---
tags:
  - RTL9607C
  - Table
  - Table Fields
---

# RTL9607C table: TCAM_RAW_TABLE_PATH3_5

## Details

*Name* TCAM_RAW_TABLE_PATH3_5

*Feature* [TABLE_ACCESS](../../feature/TABLE_ACCESS)

*Type* 13

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
|I_DPORT|119|16||
|I_SPORT|103|16||
|I_DIP_LSB|71|32||
|I_SIP_LSB|39|32||
|I_L4_PTC|38|1||
|I_IPV4_6|37|1||
|PPP_ID|21|16||
|I_TOS|13|8||
|PPPOE_IF|12|1||
|STAG_IF|11|1||
|CTAG_IF|10|1||
|MACT|9|1||
|PTH|0|2||
