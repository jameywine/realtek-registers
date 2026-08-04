---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: EPON_RGSTR2

## Details

*Name* EPON_RGSTR2

*Offset* 0x36010

*Feature* [EPON_CONFIGURATION](../../feature/EPON_CONFIGURATION)

## Description

register request configuration register 2

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:9|RESERVED||
|8:1|REG_PENDDING_GRANT|register pendding grant number, max vlaue is 32|
|0|REGISTER_REQUEST|indicator ASIC must trigger register reguest|
