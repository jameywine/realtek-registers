---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: EPON_TIME_CTRL

## Details

*Name* EPON_TIME_CTRL

*Offset* 0x36034

*Feature* [EPON_CONFIGURATION](../../feature/EPON_CONFIGURATION)

## Description

RTT and time control register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:22|RESERVED||
|21:16|QUARD_THRESHOLD|This field holds the maximal amount of drift allowed for a timestamp received at the ONU.<br>0b0 4 time quanta.<br>0b1 8 time quanta. (Default)<br>0b2 16tim quanta.<br>0b3 32time quanta.|
|15:0|RTT_ADJ|RTT adjust. Unit (TQ)<br>The value is signed interger.<br>This reguster use to adjust the RTT value for RTT emulation.<br>The timestamp from OLT will be adjust by this register then update to local time.|
