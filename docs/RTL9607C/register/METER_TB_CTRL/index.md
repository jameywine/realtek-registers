---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: METER_TB_CTRL

## Details

*Name* METER_TB_CTRL

*Offset* 0x25000

*Feature* [METER_MARKER](../../feature/METER_MARKER)

## Description

Specify the tick time of the leaky bucket for a meter block. Unit: clock.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:17|RESERVED||
|16|METER_OP|0b0: Can’t consume token exceed requirement<br>0b1: consume token exceed requirement, and return to 0.|
|15:8|TICK_PERIOD|Meter bucket refresh timing tick, uint 1/system clock frequency. Default value should be set with different chip mode.|
|7:0|TKN|Refresh bytes counter of shared meter. The shared meter TICK and COUNTER should be assigned to matched refresh speed as 8kbps. Default value should be set with different chip mode.|
