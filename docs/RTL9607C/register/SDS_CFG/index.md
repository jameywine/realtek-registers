---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: SDS_CFG

## Details

*Name* SDS_CFG

*Offset* 0x270

*Feature* [CHP_INFORMATION](../../feature/CHP_INFORMATION)

*Bit Offset:* 32

*Port Range:* 0-2

## Description

Serdes Configuration register.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:7|RESERVED||
|6|CFG_SDS_SG_LIMT||
|5|CFG_COMBO_SDS_EN||
|4:0|CFG_SDS_MODE|Serdes mode.<br>0x1f - Off<br>0x16 - 2500BASEX<br>0x12 - HSGMII<br>0xc - EPON<br>0x8 - GPON<br>0x7 - Fiber Auto<br>0x5 Fiber 100M<br>0x4 - Fiber 1G<br>0x2 - SGMII 1G|
