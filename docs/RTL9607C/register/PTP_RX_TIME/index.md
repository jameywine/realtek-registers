---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: PTP_RX_TIME

## Details

*Name* PTP_RX_TIME

*Offset* 0x11110

*Feature* [PTP_PRECISION_TIME_PROTOCOL_](../../feature/PTP_PRECISION_TIME_PROTOCOL_)

*Bit Offset:* 64

## Description

Get the Tx timestamp of the last transmitted PTP packet on a port.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|63:35|RESERVED||
|34:32|SEC_2_0|second bits 31 0 of PTP latching time|
|31:30|RESERVED||
|29:3|NSEC_UNIT|8 nano-second bits of PTP latching time|
|2:0|RESERVED||
