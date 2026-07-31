---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: SERI_LED_REFRESH_TIME

## Details

*Name* SERI_LED_REFRESH_TIME

*Offset* 0x1E070

*Feature* [LED](../../feature/LED)

## Description

Serial LED Refresh Register.

The refresh time of serial mode LED would be controlled by following register.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:2|RESERVED||
|1:0|CFG_SERI_LED_REGRESH_TIME|select serial LED refresh time<br>00 = 16 ms<br>01 = 32 ms<br>10 = 64 ms (default)<br>11 = 128 ms|
