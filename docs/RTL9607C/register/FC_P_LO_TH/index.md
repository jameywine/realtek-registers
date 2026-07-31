---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: FC_P_LO_TH

## Details

*Name* FC_P_LO_TH

*Offset* 0x231B8

*Feature* [FLOWCONTROL_BACKPRESSURE_THRESHOLD](../../feature/FLOWCONTROL_BACKPRESSURE_THRESHOLD)

## Description

Specify per port low on/off threshold when flow control on.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:26|RESERVED||
|25:16|ON_TH|Port based reserved threshold for turn on flow control|
|15:10|RESERVED||
|9:0|OFF_TH|Port based reserved threshold for turn off flow control|
