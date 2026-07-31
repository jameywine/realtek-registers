---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: FC_P_HI_TH

## Details

*Name* FC_P_HI_TH

*Offset* 0x231B4

*Feature* [FLOWCONTROL_BACKPRESSURE_THRESHOLD](../../feature/FLOWCONTROL_BACKPRESSURE_THRESHOLD)

## Description

Specify per port high on/off threshold when flow control on.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:26|RESERVED||
|25:16|ON_TH|port based threshold for turn on flow control|
|15:10|RESERVED||
|9:0|OFF_TH|Port based threshold for turn off flow control|
