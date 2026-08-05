---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GEM_US_PTN_CTRL

## Details

*Name* GPON_GEM_US_PTN_CTRL

*Offset* 0x706054

*Feature* [GEM_UPSTREAM](../../feature/GEM_UPSTREAM)

## Description

GEM upstream pattern control register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:21|RESERVED||
|20|EOB_MERGE_DIS||
|19:17|RESERVED||
|16|DEBUG_BUS_SEL|Mux of GEM US debug bus|
|15:14|RESERVED||
|13:12|GEM_PTN_MODE|0: normal GEM data from switch<br>1: force idle<br>2:fore increasing bytes<br>3: use the fixed patter specified in GEM_pattern_byte|
|11:8|RESERVED||
|7:0|GEM_PTN_BYTE|Used for upstream GEM data in case GEM_pattern_mode == 3|
