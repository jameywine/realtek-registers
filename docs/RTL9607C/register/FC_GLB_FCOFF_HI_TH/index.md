---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: FC_GLB_FCOFF_HI_TH

## Details

*Name* FC_GLB_FCOFF_HI_TH

*Offset* 0x231A4

*Feature* [FLOWCONTROL_BACKPRESSURE_THRESHOLD](../../feature/FLOWCONTROL_BACKPRESSURE_THRESHOLD)

## Description

Specify global high on/off threshold when flow contrl off.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:26|RESERVED||
|25:16|ON_TH|System based threshold for starting to drop packet|
|15:10|RESERVED||
|9:0|OFF_TH|System based threshold for stopping to drop packet|
