---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: METER_GLB_CTRL

## Details

*Name* METER_GLB_CTRL

*Offset* 0x25004

*Feature* [METER_MARKER](../../feature/METER_MARKER)

*Bit Offset:* 64

*Array Range:* 0-47

## Description

Share meter global control register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|63:51|RESERVED||
|50:32|RATE|Meter rate,unit: 8Kbps (K=1024)<br>19’h7ffff : BW= full rate (line rate)<br>N : BW=N*8Kbps|
|31:18|RESERVED||
|17|TYPE|Meter mode.<br>0: Bit rate mode.<br>1: Packet rate mode.|
|16:1|BUCKET_SIZE|Bucket size of shared meter|
|0|IFG|Share meter rate calculation with 20 bytes IPG|
