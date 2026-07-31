---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: FC_PUB_FCOFF_USED_PAGE_CNT

## Details

*Name* FC_PUB_FCOFF_USED_PAGE_CNT

*Offset* 0x231D0

*Feature* [FLOWCONTROL_BACKPRESSURE_THRESHOLD](../../feature/FLOWCONTROL_BACKPRESSURE_THRESHOLD)

## Description

Specify public used page count include maximum and dynamic used page count when flow control off.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:26|RESERVED||
|25:16|PUB_FCOFF_MAX_USED_PAGE_CNT|This register can latch the maximum public used page count in dropping mode|
|15:10|RESERVED||
|9:0|PUB_FCOFF_USED_PAGE_CNT|This register can indicate the public used page count dynamic in dropping mode|
