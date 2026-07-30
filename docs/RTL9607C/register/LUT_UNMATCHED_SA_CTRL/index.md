---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: LUT_UNMATCHED_SA_CTRL

## Details

*Name* LUT_UNMATCHED_SA_CTRL

*Offset* 0x1C000

*Feature* [ADDRESS_TABLE_LOOKUP](../../feature/ADDRESS_TABLE_LOOKUP)

*Bit Offset:* 2

*Port Range:* 0-10

## Description

unmatched SA control register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|1:0|ACT|Drop/Trap packet if SA is not from the same source port as L2 SPA<br>0b00: normal<br>0b01: drop packet & disable learning<br>0b10: trap to CPU<br>0b11: copy to CPU|
