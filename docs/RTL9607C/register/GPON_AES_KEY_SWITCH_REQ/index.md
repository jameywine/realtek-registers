---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_AES_KEY_SWITCH_REQ

## Details

*Name* GPON_AES_KEY_SWITCH_REQ

*Offset* 0x703010

*Feature* [AES_DECRYPT](../../feature/AES_DECRYPT)

## Description

AES key switch request

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15|KEY_CFG_REQ|CPU write 0x0 then 0x1 to this bit to request AES key switch.|
|14|CFG_ACTIVE_KEY|0x0: The shadow key will be written.<br>0x1: Active key will be change - please note this would hit the traffic and should never be used during normal operations.<br>Software should always write to the shadow key in normal operation.|
|13:0|RESERVED||
