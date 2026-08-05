---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_RESET

## Details

*Name* GPON_RESET

*Offset* 0x70000C

*Feature* [GPON_MAC_GENERAL_CONFIG](../../feature/GPON_MAC_GENERAL_CONFIG)

## Description

GPON MAC reset and status

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:9|RESERVED||
|8|RST_DONE|0x0: the reset action is not done or the reset action is not triggered<br>0x1: Reset done. GPON MAC functions when RST_DONE = 1. Once GPON MAC is reset, either by hardware or software reset, this status register will be cleared automatically then be set after 30 cycles (in VCI bus clock). Value 1 of this register means that GPON MAC is ready to operate, and software can configure other registers.|
|7:1|RESERVED||
|0|SOFT_RST|Software writes 1 to this bit to reset all GPON MAC logics and clear all registers.|
