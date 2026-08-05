---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GEM_US_BYTE_STAT

## Details

*Name* GPON_GEM_US_BYTE_STAT

*Offset* 0x706800

*Feature* [GEM_UPSTREAM](../../feature/GEM_UPSTREAM)

*Bit Offset:* 64

*Array Range:* 0-127

## Description

GEM upstream byte statistics counter

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|63:32|CNTR_LOW32|The low 32 bits of data bytes counter by the local Port Index.<br>The array index map to the local Port Index.|
|31:0|CNTR_HIGH32|The high 32 bits of data bytes counter by the local Port Index.<br>The array index map to the local Port Index.|
