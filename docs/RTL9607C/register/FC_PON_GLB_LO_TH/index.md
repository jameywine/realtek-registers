---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: FC_PON_GLB_LO_TH

## Details

*Name* FC_PON_GLB_LO_TH

*Offset* 0x23204

*Feature* [FLOWCONTROL_BACKPRESSURE_THRESHOLD](../../feature/FLOWCONTROL_BACKPRESSURE_THRESHOLD)

## Description

Specify PON MAC global low on/off threshold when flow contrl on.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:26|RESERVED||
|25:16|ON_TH|PON MAC Shared based threshold for turn on flow control|
|15:10|RESERVED||
|9:0|OFF_TH|PON MAC Shared based threshold for turn off flow control|
