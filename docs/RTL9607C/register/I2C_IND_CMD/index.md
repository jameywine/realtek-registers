---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: I2C_IND_CMD

## Details

*Name* I2C_IND_CMD

*Offset* 0xC4

*Feature* [INTERFACE](../../feature/INTERFACE)

*Bit Offset:* 32

*Array Range:* 0-1

## Description

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:4|RESERVED||
|3|SLV_NACK||
|2|BUSY|1: busy, read/write command is not finish.|
|1|RW_EN|write enable. 0: read, 1: write|
|0|CMD_EN|command enable and auto clear. Check the BUSY bit to make sure the command is done.|
