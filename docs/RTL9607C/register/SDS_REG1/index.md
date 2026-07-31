---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: SDS_REG1

## Details

*Name* SDS_REG1

*Offset* 0x40804

*Feature* [PHY_SERDES](../../feature/PHY_SERDES)

## Description

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15|SP_CFG_PTR_ERR_EN||
|14|SP_CFG_AUTO_10BIT||
|13|SP_CFG_FULL_ACK2||
|12|SP_CFG_NXP_EN||
|11:8|SP_SDS_FRC_RX|serdes force RX for 4-port<br>0: disable N-way (force RX)<br>1: enable N-way|
|7|SP_CFG_HSG_RTIG||
|6|SP_CFG_XSG||
|5|SP_CFG_FRC_DWSPD||
|4|SP_CFG_DIS_8B10B_PWR_OPT||
|3:0|SP_SDS_FRC_TX|serdes force TX for 4-port<br>0: normal<br>1: force TX, even if not receive any signal|
