---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: PON_TB_CTRL

## Details

*Name* PON_TB_CTRL

*Offset* 0xF021DC

*Feature* [PONIP_SCHEDULING_UPSTREAM](../../feature/PONIP_SCHEDULING_UPSTREAM)

## Description

Specify the tick time in PON MAC. Unit: clock.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15:8|TKN|Refresh bytes counter of shared meter for PON port. The shared meter TICK and COUNTER should be assigned to matched refresh speed as 64kbps. Default value should be set with different chip mode.|
|7:0|TICK_PERIOD|Meter bucket refresh timing tick for PON port, uint 1/system clock frequency. Default value should be set with different chip mode.|
