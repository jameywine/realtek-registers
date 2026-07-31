---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: SERI_LED_CLK_PER

## Details

*Name* SERI_LED_CLK_PER

*Offset* 0x1E06C

*Feature* [LED](../../feature/LED)

## Description

Serial LED Clock Register

The serial LED output clock period would be controlled by this register.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:2|RESERVED||
|1:0|CFG_SERI_LED_CLK_PER|select clock period<br>00 = 3.9MHz(256ns)<br>01 = 7.8MHz(128ns) (default)<br>10 = 15.62MHz(64ns)<br>11 = 15.62MHz(64ns)|
