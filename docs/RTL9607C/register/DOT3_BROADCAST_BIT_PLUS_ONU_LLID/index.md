---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: DOT3_BROADCAST_BIT_PLUS_ONU_LLID

## Details

*Name* DOT3_BROADCAST_BIT_PLUS_ONU_LLID

*Offset* 0x32E94

*Feature* [STATISTIC_COUNTERS](../../feature/STATISTIC_COUNTERS)

## Description

dot3OmpEmulationBroadcastBitPlusOnuLlid

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:0|BROADCASTBITPLUSONULLID|A count of frames received that contain a valid SLD field, pass the CRC-8 check, and contain the broadcast bit in the LLID and match the ONU’s LLID (frame reflected)<br>(mode is broadcast, but LLID not equal to 0x7FFF and ONU’s LLID)this kind of packet wii be droped|
