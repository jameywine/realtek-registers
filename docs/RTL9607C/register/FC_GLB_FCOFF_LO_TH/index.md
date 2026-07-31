---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: FC_GLB_FCOFF_LO_TH

## Details

*Name* FC_GLB_FCOFF_LO_TH

*Offset* 0x231A8

*Feature* [FLOWCONTROL_BACKPRESSURE_THRESHOLD](../../feature/FLOWCONTROL_BACKPRESSURE_THRESHOLD)

## Description

Specify global low on/off threshold when flow contrl off.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:26|RESERVED||
|25:16|ON_TH|Shared based threshold for starting to drop packet|
|15:10|RESERVED||
|9:0|OFF_TH|Shared based threshold for stopping to drop packet|
