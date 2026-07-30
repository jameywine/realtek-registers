---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: UNKN_L2_MC

## Details

*Name* UNKN_L2_MC

*Offset* 0x1C018

*Feature* [ADDRESS_TABLE_LOOKUP](../../feature/ADDRESS_TABLE_LOOKUP)

*Bit Offset:* 2

*Port Range:* 0-10

## Description

unknow L2 multicast register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|1:0|ACT|unknow L2 multicast frame behavior<br>0b00: normal flooding<br>0b01: drop packet<br>0b10: trap to CPU<br>0b11: drop packet exclude RMA|
