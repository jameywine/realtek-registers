---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: LUT_UNKN_UC_DA_CTRL

## Details

*Name* LUT_UNKN_UC_DA_CTRL

*Offset* 0x1C00C

*Feature* [ADDRESS_TABLE_LOOKUP](../../feature/ADDRESS_TABLE_LOOKUP)

*Bit Offset:* 2

*Port Range:* 0-10

## Description

unknown unicast DA control register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|1:0|ACT|Drop/Trap packet if unicast DA is unknown<br>0b00: normal flooding<br>0b01: drop packet, exclude IGMP/MLD packets<br>0b10: trap to CPU, exclude IGMP/MLD packets<br>0b11: reserved|
