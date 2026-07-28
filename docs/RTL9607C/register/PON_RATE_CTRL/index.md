---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: PON_RATE_CTRL

## Details

*Name* PON_RATE_CTRL

*Offset* 0x2D990

*Feature* [OTHER](../../feature/OTHER)

## Description

PON Port rate control

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:20|RESERVED||
|19|EN_RATE_PON|Enable PON rate control|
|18:0|RATE|PON rate control, unit: 8Kbps (K=1024)<br>N : BW=N*8Kbps|
