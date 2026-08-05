---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_AES_INTR_MASK

## Details

*Name* GPON_AES_INTR_MASK

*Offset* 0x703004

*Feature* [AES_DECRYPT](../../feature/AES_DECRYPT)

## Description

AES intrrupt indicator

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:2|RESERVED||
|1|INFO_FIFO_OVERFL_M|0x0: Disable INFO_FIFO_OVERFL_DLT to generate inrerrupt.<br>0x1: Enable INFO_FIFO_OVERFL_DLT to generate inrerrupt.|
|0|DATA_FIFO_OVERFL_M|0x0: Disable DATA_FIFO_OVERFL_DLT to generate inrerrupt.<br>0x1: Enable DATA_FIFO_OVERFL_DLT to generate inrerrupt.|
