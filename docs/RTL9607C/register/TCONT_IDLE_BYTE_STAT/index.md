---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: TCONT_IDLE_BYTE_STAT

## Details

*Name* TCONT_IDLE_BYTE_STAT

*Offset* 0x706C00

*Feature* [GEM_UPSTREAM](../../feature/GEM_UPSTREAM)

*Bit Offset:* 64

*Array Range:* 0-31

## Description

GEM upstream idle statistics counter

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|63:32|CNTR_LOW32|The low 32 bits of IDLE bytes counter by the local TCONT Index.<br>The array index map to the local TCONT Index.|
|31:0|CNTR_HIGH32|The high 32 bits of IDLE bytes counter by the local TCONT Index.<br>The array index map to the local TCONT Index.|
