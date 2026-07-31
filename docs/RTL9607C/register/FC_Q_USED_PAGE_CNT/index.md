---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: FC_Q_USED_PAGE_CNT

## Details

*Name* FC_Q_USED_PAGE_CNT

*Offset* 0x2D06C

*Feature* [FLOWCONTROL_BACKPRESSURE_THRESHOLD](../../feature/FLOWCONTROL_BACKPRESSURE_THRESHOLD)

*Bit Offset:* 32

*Array Range:* 0-7

*Port Range:* 0-10

## Description

Specify the output queue used page count include maximum and dynamic used page count.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:26|RESERVED||
|25:16|Q_MAX_USED_PAGE_CNT|maximum used page counts for output queue on each port.|
|15:10|RESERVED||
|9:0|Q_USED_PAGE_CNT|Dynamic used page counts for output queue on each port.|
