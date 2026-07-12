---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: BOND_INFO

## Details

*Name* BOND_INFO

*Offset* 0x10008

*Feature* [CHP_INFORMATION](../../feature/CHP_INFORMATION)

## Description

Specify the chip bonding information.
It is used to get Chip Subtype information.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:28|BOND_INFO_EN|Enable Bond Information display.<br>0xB: enable.<br>Others: disable.<br>Note: BOND_INFO only can be read when BOND_INFO_EN{3:0}=0xB, otherwise the read result will return 0x0.|
|27:5|RESERVED||
|4:0|BOND_CHIP_MODE|bound chip mode/Chip Subtype|
