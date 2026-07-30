---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: LUT_LEARN_OVER_CTRL

## Details

*Name* LUT_LEARN_OVER_CTRL

*Offset* 0x1C010

*Feature* [ADDRESS_TABLE_LOOKUP](../../feature/ADDRESS_TABLE_LOOKUP)

*Bit Offset:* 2

*Port Range:* 0-10

## Description

LUT learning over control register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|1:0|ACT|Auto leaning number exceed behavior<br>0b00: normal flooding<br>0b01: drop packet<br>0b10: trap to CPU<br>0b11: copy to cpu|
