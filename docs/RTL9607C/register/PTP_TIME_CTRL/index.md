---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: PTP_TIME_CTRL

## Details

*Name* PTP_TIME_CTRL

*Offset* 0x1B01C

*Feature* [PTP_PRECISION_TIME_PROTOCOL_](../../feature/PTP_PRECISION_TIME_PROTOCOL_)

## Description

The register can be used to operate the time of reference time clock.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:4|RESERVED||
|3|PPS_EN|PTP PPS Enable|
|2|TOD_EN|PON ToD Enable|
|1|PTP_TIME_LATCH|Latch current time to PTP_TIME_SEC and PTP_TIME_NSEC|
|0|CMD|Enable system time tuning with system offset timer, write to clear|
