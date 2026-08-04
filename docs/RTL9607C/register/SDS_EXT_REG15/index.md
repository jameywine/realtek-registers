---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: SDS_EXT_REG15

## Details

*Name* SDS_EXT_REG15

*Offset* 0x40A3C

*Feature* [PHY_SERDES](../../feature/PHY_SERDES)

## Description

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15|SEP_CFG_EPON_PWRCTL||
|14:11|SEP_CFG_LP_CNT_1|Set to 0x2 by SDK with "FEC must check this setting". Only for EPON mode.|
|10|SEP_CFG_DIS_FECK_SPUP|Bit is set by SDK with "FEC must check this setting". Only for EPON mode.|
|9:0|SEP_CFG_DX|Set to 0x162 by SDK with "FEC must check this setting". Only for EPON mode.|
