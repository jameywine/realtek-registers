---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: LED_FORCE_VALUE_CFG

## Details

*Name* LED_FORCE_VALUE_CFG

*Offset* 0x1E054

*Feature* [LED](../../feature/LED)

*Bit Offset:* 2

*Array Range:* 0-17

## Description

CPU Force LED Register

LED also can force by CPU by setting LED source to CPU force mode. The force value can be controlled by this register.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|1:0|SEL_LED_FORCE_VALUE|00: force 0<br>01: force 1<br>10: force blinking<br>11: reserved|
