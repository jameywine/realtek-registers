---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_BWMAP_CTRL

## Details

*Name* GPON_BWMAP_CTRL

*Offset* 0x70200C

*Feature* [BWMAP_CAPTURE](../../feature/BWMAP_CAPTURE)

## Description

BWMAP control register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15|CAP_EN|Write 0x0 then 0x1 to start BWMAP capture.|
|14|CAP_CLR|Write 0x0 then 0x1 to clear BWMAP capture buffer.|
|13:8|RESERVED||
|7:0|CAP_FRAME_NUM|Capture BWMAP in N GPON frames.|
