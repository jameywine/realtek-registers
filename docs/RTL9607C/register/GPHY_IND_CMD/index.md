---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPHY_IND_CMD

## Details

*Name* GPHY_IND_CMD

*Offset* 0x4

*Feature* [INTERFACE](../../feature/INTERFACE)

## Description

GPHY indirect command and address

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:23|RESERVED||
|22|WREN|write enable.<br>0: read, 1: write|
|21|CMD_EN|command enable and auto clear. Check the BUSY bit to make sure the command is done.|
|20:0|ADR|read/write address<br>{20:16}=phyid; {15:0}=reg address|
