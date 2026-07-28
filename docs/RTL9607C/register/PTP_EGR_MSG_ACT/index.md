---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: PTP_EGR_MSG_ACT

## Details

*Name* PTP_EGR_MSG_ACT

*Offset* 0x1110C

*Feature* [PTP_PRECISION_TIME_PROTOCOL_](../../feature/PTP_PRECISION_TIME_PROTOCOL_)

*Bit Offset:* 2

*Array Range:* 0-9

## Description

Egress action config for PTP message class

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|1:0|ACT|Action foregress PTP message class x(0-7)<br>0b00: none<br>0b01: Latch egress timestamp<br>0b10: Latch egress timestamp and Tx mirror to CPU with PTP timestamp CPU-tag<br>0b11: Modify correctionField|
