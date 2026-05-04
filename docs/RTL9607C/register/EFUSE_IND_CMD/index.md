---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: EFUSE_IND_CMD

## Details

*Name* EFUSE_IND_CMD

*Offset* 0x1C

*Feature* [INTERFACE](../../feature/INTERFACE)

## Description

eFuse indirect command and address

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:24|RESERVED||
|23:20|MODE_SEL||
|19:18|RESERVED||
|17|WREN|write enable.<br>0: read, 1: write|
|16|CMD_EN|command enable and auto clear. Check the BUSY bit to make sure the command is done.|
|15:0|ADR|read/write address|
