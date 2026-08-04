---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: SDS_EXT_REG12

## Details

*Name* SDS_EXT_REG12

*Offset* 0x40A30

*Feature* [PHY_SERDES](../../feature/PHY_SERDES)

## Description

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15:13|SEP_CFG_PRBS_SEED||
|12|SEP_CFG_FEC_PRBS_MD||
|11|SEP_CFG_PRBS_ON|Set 1 to enable force PRBS?|
|10|SEP_CFG_FIFO_RESTORE||
|9|SEP_CFG_ASDS_RST||
|8|SEP_CFG_NEG_CLKRD_D2A|Set to 1 by SDK when force PRBS is enabled.|
|7|SEP_CFG_FIFO_ORG||
|6|SEP_CFG_FRXNRZI_SEL||
|5|SEP_CFG_SCR_SEED_SEL||
|4|SEP_CFG_XSG257_NO_CLKGAT||
|3|SEP_CFG_XSG_OFF_AFE1||
|2:0|SEP_CFG_IPG_CNT|Set to 0x3 when force PRBS is enabled and 0x5 when PRBS is off. Also set to 0x3 during EPON mode setting as a "PCS Serdes patch"|
