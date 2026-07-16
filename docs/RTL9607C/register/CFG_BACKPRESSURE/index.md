---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: CFG_BACKPRESSURE

## Details

*Name* CFG_BACKPRESSURE

*Offset* 0x23100

*Feature* [MAC_CONTROL](../../feature/MAC_CONTROL)

## Description

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:4|RESERVED||
|3|DROP_48_PASS_1||
|2|LONGTXE|carrierbased back-pressure<br>0:collision based back-pressure<br>carrier based back-pressure, defer mode with 2K bytes TX_EN|
|1|RESERVED||
|0|EN_48_PASS_1|Enable 48-pass-1<br>0: disable<br>1:enable|
