---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: METER_LB_EXCEED_STS

## Details

*Name* METER_LB_EXCEED_STS

*Offset* 0x25184

*Feature* [METER_MARKER](../../feature/METER_MARKER)

*Bit Offset:* 1

*Array Range:* 0-47

## Description

meter leaky buckets exceeding status. A bit would be set to 1 for a meter if it satisfies "drop packet" or "color packet red". It is write 1 to clear.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|0|LB_EXCEED|1 bit flag per meter entry to show if the meter entry ever drops a packet or color a packet to red. Write 1 to clear.<br>0b0: no packet is dropped or colored red by this meter<br>0b1: some packets are ever dropped or colored red by this meter|
