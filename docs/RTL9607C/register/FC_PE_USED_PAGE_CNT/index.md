---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: FC_PE_USED_PAGE_CNT

## Details

*Name* FC_PE_USED_PAGE_CNT

*Offset* 0x2D040

*Feature* [FLOWCONTROL_BACKPRESSURE_THRESHOLD](../../feature/FLOWCONTROL_BACKPRESSURE_THRESHOLD)

*Bit Offset:* 32

*Port Range:* 0-10

## Description

Specify per egress port used page count include maximum and dynamic used page count.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:26|RESERVED||
|25:16|PE_MAX_USED_PAGE_CNT|This register can latch the maximum used page RO count of egress port.|
|15:10|RESERVED||
|9:0|PE_USED_PAGE_CNT|This register can indicate dynamic used page count of egress port.|
