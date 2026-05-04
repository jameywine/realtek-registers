---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: CFG_PCSXF

## Details

*Name* CFG_PCSXF

*Offset* 0x44

*Feature* [INTERFACE](../../feature/INTERFACE)

## Description

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:15|RESERVED||
|14:10|RST_RXFIFO|reset rx sync. fifo. 1: reset, 0: normal|
|9:5|CFG_MIIRX_IPG||
|4:1|CFG_PCSXF|bit 4: sel_org_crs<br>bit 3: sel_org_col bit<br>2: reserved (phy mode)<br>bit 1: skip rxer|
|0|COL_10M|assert rxdv when col asserts in half-dup and 10M|
