---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: CHIP_INFO

## Details

*Name* CHIP_INFO

*Offset* 0x10004

*Feature* [CHP_INFORMATION](../../feature/CHP_INFORMATION)

## Description

Specify the chip information.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:28|CHIP_INFO_EN|Enable Chip Information display.<br>0xA: enable.<br>Others: disable.<br>Note: CHIP_INFO only can be read when CHIP_INFO_EN{3:0}=0xA, otherwise the read result will return 0x0.|
|27:21|RESERVED||
|20:16|CHIP_VER|Chip version.<br>0x0: NULL character<br>0x1-0x1A: character A - Z<br>0x1B-0x1F: invalid|
|15:0|RL_ID|RL CPU number|
