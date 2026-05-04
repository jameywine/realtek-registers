---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: SOFTWARE_RST

## Details

*Name* SOFTWARE_RST

*Offset* 0x108

*Feature* [RESET](../../feature/RESET)

## Description

Software reset register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:17|RESERVED||
|16|CMD_WRAP_EX1_RST_PS||
|15|DYING_RST_POL||
|14|DYING_RST_EN||
|13|CMD_NRESET_LOW||
|12|CMD_WRAP_EX0_RST_PS||
|11|PONMAC_RST|PON MAC software reset.|
|10|SW_RST|Set 1 to issue global switch software reset. Will auto clear upon completion. |
|9|CMD_SWSYS_RST_PS|Reset switch system? |
|8|CMD_CFG_RST_PS|Reset config? |
|7|CMD_CHIP_RST_PS|1: Reset switch chip|
|6|CMD_GPHY_RST_PS|1: Reset GPHY|
|5:3|CMD_SDS_CFG_RST_PS|Reset serdes config? |
|2:0|CMD_SDS_RST_PS|1: Reset serdes which includes digital, analog and GPON MAC|
