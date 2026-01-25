---
tags:
  - RTL9607C
  - Table
  - Table Fields
---

# RTL9607C table: FLOW_TABLE_PATH6

## Details

*Name* FLOW_TABLE_PATH6

*Feature* [TABLE_ACCESS](../../feature/TABLE_ACCESS)

*Type* 8

*Entries* 4096

*Control register* [NAT_TBL_ACCESS_CTRL](../../register/NAT_TBL_ACCESS_CTRL)

*Write Data register* [NAT_TBL_ACCESS_WR_DATA](../../register/NAT_TBL_ACCESS_WR_DATA)

*Read Data register* [NAT_TBL_ACCESS_RR_DATA](../../register/NAT_TBL_ACCESS_RR_DATA)

## Description

## Fields

|Name|LSB|Bits|Description|
| :--- | :--- | :--- | :--- |
|I_CPRI|221|3||
|LOCK|220|1||
|I_DSCP_CHK|219|1||
|I_GRE_ID_CHK|218|1||
|O_DROP|208|1||
|I_L2_SSN_ID|176|16||
|I_L2_TNL_ID|160|16||
|I_DA_IDX|148|12||
|I_SA_IDX|136|12||
|I_PTC|128|4||
|I_DPORT|112|16||
|I_SPORT|96|16||
|I_DIP_LSB|64|32||
|I_SIP_LSB|32|32||
|I_TOS|24|8||
|I_PPPOE_IF|19|1||
|I_STAG_IF|18|1||
|I_CTAG_IF|17|1||
|I_IPV4_6|16|1||
|I_DIP_CHK|15|1||
|I_SIP_CHK|14|1||
|I_DMAC_CHK|13|1||
|I_SMAC_CHK|12|1||
|I_L2_SSN_ID_CHK|11|1||
|I_L2_TNL_ID_CHK|10|1||
|I_DPORT_CHK|9|1||
|I_SPORT_CHK|8|1||
|I_IF_IDX|4|4||
|PTH|2|2||
|VALID|0|1||
