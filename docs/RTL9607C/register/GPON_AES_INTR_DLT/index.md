---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_AES_INTR_DLT

## Details

*Name* GPON_AES_INTR_DLT

*Offset* 0x703000

*Feature* [AES_DECRYPT](../../feature/AES_DECRYPT)

## Description

AES intrrupt indicator

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15|AES_DECRYPT_INTR|Interrupt status of the AES module.<br>AES_DECRYPT_PAGE = (INFO_FIFO_OVERF_DLT and INFO_FIFO_OVERF_M) or (DATA_FIFO_OVERF_DLT and DATA_FIFO_OVERF_M);|
|14:2|RESERVED||
|1|INFO_FIFO_OVERFL_DLT|INFO_FIFO_OVERFL has changed since last time of reading.|
|0|DATA_FIFO_OVERFL_DLT|DATA_FIFO_OVERFL has changed since last time of reading.|
