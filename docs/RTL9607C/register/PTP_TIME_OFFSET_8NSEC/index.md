---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: PTP_TIME_OFFSET_8NSEC

## Details

*Name* PTP_TIME_OFFSET_8NSEC

*Offset* 0x1B014

*Feature* [PTP_PRECISION_TIME_PROTOCOL_](../../feature/PTP_PRECISION_TIME_PROTOCOL_)

## Description

nanosecond offset tuning of PTP reference time clock.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:30|RESERVED||
|29:3|NSEC_UNIT|offset nanosecond in the reference time clock.<br>(Unit: 8 nanoseconds)|
|2:0|RESERVED||
