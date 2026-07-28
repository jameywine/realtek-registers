---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: PTP_IGR_MSG_ACT

## Details

*Name* PTP_IGR_MSG_ACT

*Offset* 0x11108

*Feature* [PTP_PRECISION_TIME_PROTOCOL_](../../feature/PTP_PRECISION_TIME_PROTOCOL_)

*Bit Offset:* 2

*Array Range:* 0-9

## Description

Ingress action config for PTP message class

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|1:0|ACT|Action for ingress PTP message class x(0-7)<br>0b00: none<br>0b01: trap to CPU with PTP timestamp CPU-tag<br>0b10: Forward to transparent active port mask<br>0b11: Forward to transparent active port mask and Rx mirror to CPU with PTP timestamp CPU-tag|
