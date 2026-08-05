---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GTC_DS_LOS_CFG_STS

## Details

*Name* GPON_GTC_DS_LOS_CFG_STS

*Offset* 0x701040

*Feature* [GTC_DOWNSTREAM](../../feature/GTC_DOWNSTREAM)

## Description

LOS configuration and status

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:11|RESERVED||
|10|CDR_LOS_SIG|Status of LOS signal input from CDR.|
|9|RESERVED||
|8|OPTIC_LOS_SIG|Status of LOS signal input from OPTIC.|
|7:5|RESERVED||
|4|LOS_FILTER_EN|0x0: Disable LOS filtering and holdover.<br>0x1: Enable LOS holdover function. If its enabled, LOS will only be raised after being stable for more than 1ms.|
|3|CDR_LOS_POLAR|CDR LOS input polarity.|
|2|CDR_LOS_EN|0x0: Disable CDR LOS input.<br>0x1: Enable CDR LOS input.|
|1|OPTIC_LOS_POLAR|Optical LOS input polarity.|
|0|OPTIC_LOS_EN|0x0: Disable optical LOS input.<br>0x1: Enable optical LOS input.|
