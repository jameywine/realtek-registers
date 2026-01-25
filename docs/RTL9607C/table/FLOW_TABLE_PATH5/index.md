---
tags:
  - RTL9607C
  - Table
  - Table Fields
---

# RTL9607C table: FLOW_TABLE_PATH5

## Details

*Name* FLOW_TABLE_PATH5

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
|O_MIB_ADR|225|5||
|O_MIB_ACT|224|1||
|I_CPRI|221|3||
|LOCK|220|1||
|I_DSCP_CHK|219|1||
|I_L4_PTC|218|1||
|O_SP2C_ACT|214|2||
|O_QID_ACT|213|1||
|O_STAG_ACT|212|1||
|O_CTAG_ACT|211|1||
|O_EGS_SID_ACT|210|1||
|O_EGS_CID_ACT|209|1||
|O_DROP|208|1||
|O_DSCP|202|6||
|O_DSCP_ACT|201|1||
|O_L4_ACT|200|1||
|IO_STM_IDX|193|7||
|O_L4_DIR|192|1||
|O_CVID|180|12||
|O_CPRI|177|3||
|O_CPRI_ACT|176|1||
|O_SVID|164|12||
|O_SPRI|161|3||
|O_SPRI_ACT|160|1||
|O_L4_PORT|144|16||
|O_EX_TAG_IDX|141|3||
|O_CVID_ACT|140|1||
|O_QID|137|3||
|O_SVID_ACT|136|1||
|O_DMAC_IDX|128|8||
|I_DPORT|112|16||
|I_SPORT|96|16||
|I_DIP_LSB|64|32||
|I_SIP_LSB|32|32||
|I_TOS|24|8||
|O_IF_IDX|20|4||
|I_PPPOE_IF|19|1||
|I_STAG_IF|18|1||
|I_CTAG_IF|17|1||
|I_IPV4_6|16|1||
|O_MTR_IDX|11|5||
|O_MTR_A|10|1||
|IO_STM_IDX_CHK|8|1||
|I_IF_IDX|4|4||
|PTH|2|2||
|VALID|0|1||
