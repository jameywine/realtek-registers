---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: SW_PBO_MSTBASE

## Details

*Name* SW_PBO_MSTBASE

*Offset* 0xF12040

*Feature* [SWPBO](../../feature/SWPBO)

## Description

switch PBO memory base

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:0|CFG_PON_MSTBASE|Kernel allocated switch pbo memory base in a physical address form. Calculated by multiplying pbo page size (128, 258, 512), max switch page count (0x400) and 5, then adding (1 << 7) for "alignment" and putting it into kmalloc. After that convert it to physical address and write that final value to this bit field.|
