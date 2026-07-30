---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: DOT3_NOT_BROADCAST_BIT_NOT_ONU_LLID

## Details

*Name* DOT3_NOT_BROADCAST_BIT_NOT_ONU_LLID

*Offset* 0x32E90

*Feature* [STATISTIC_COUNTERS](../../feature/STATISTIC_COUNTERS)

## Description

dot3OmpEmulationNotBroadcastBitNotOnuLlid

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:0|NOTBROADCASTBITNOTONULLID|A count of frames received that contain a valid SLD field, pass the CRC-8 check, and do not contain the ONU’s LLID<br>(Mode is unicast but LLID not local ONU’s LLID ) this kind of packet will be droped|
