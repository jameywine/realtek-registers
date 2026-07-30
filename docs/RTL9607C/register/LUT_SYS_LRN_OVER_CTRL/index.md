---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: LUT_SYS_LRN_OVER_CTRL

## Details

*Name* LUT_SYS_LRN_OVER_CTRL

*Offset* 0x17040

*Feature* [ADDRESS_TABLE_LOOKUP](../../feature/ADDRESS_TABLE_LOOKUP)

## Description

LUT system learning over control register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:2|RESERVED||
|1:0|ACT|Auto leaning number exceed behavior<br>0b00: normal flooding<br>0b01: drop packet<br>0b10: trap to CPU<br>0b11: Copy to cPU|
