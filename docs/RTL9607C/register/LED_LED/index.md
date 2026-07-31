---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: LED_LED

## Details

*Name* LED_LED

*Offset* 0x1E000

*Feature* [LED](../../feature/LED)

## Description

LED Mode Register

The ASIC provide both parallel and serial LED mode, user can program either one of them as the system LED mode. ASIC supports 18 parallel and 18 serial LED groups.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:1|RESERVED||
|0|LED_SEL|configuration system led mode<br>0:parallel mode<br>1:serial mode|
