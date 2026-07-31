---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: WSDS_DIG_00

## Details

*Name* WSDS_DIG_00

*Offset* 0x40030

*Feature* [PHY_SERDES](../../feature/PHY_SERDES)

## Description

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:12|RESERVED||
|11|CFG_SFT_RSB_ANA|0: software reset sds analog<br>1: no software reset sds analog|
|10|CFG_SFT_RSTB_GPON|0: software reset gpon mac<br>1: no software reset epon_mac|
|9|CFG_SFT_RSTB_EPON|0: software reset epon mac<br>1: no software reset epon_mac|
|8|CFG_SFT_RSTB|0: software reset all wrap_sds<br>1: no software reset all wrap_sds|
|7|CFG_FRCV_155M_EN||
|6|CFG_FRC_155M_EN||
|5|CFG_FRCV_125M_EN||
|4|CFG_FRC_125M_EN||
|3|CFG_FRCV_GMIICK_EN||
|2|CFG_FRC_GMIICK_EN||
|1|CFG_TXDIS_SEL||
|0|CFG_STOP_CLK|0: no stop clock to swcore<br>1: stop clock to swcore|
