---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: PON_LED_CFG

## Details

*Name* PON_LED_CFG

*Offset* 0x1E078

*Feature* [LED](../../feature/LED)

## Description

LED active high/low Register.

When LED set to PON, it would indicate the PON status. This register can set the PON warning and alarm status.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:2|RESERVED||
|1|SWLED_PONN_ALARM|0b0: pon not in alarm state<br>0b1: pon in alarm state|
|0|SWLED_PON_WARN|0b0: pon not in warning state<br>0b1: pon in warning state|
