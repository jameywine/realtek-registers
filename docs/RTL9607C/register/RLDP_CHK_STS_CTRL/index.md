---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: RLDP_CHK_STS_CTRL

## Details

*Name* RLDP_CHK_STS_CTRL

*Offset* 0x1A004

*Feature* [RLDP](../../feature/RLDP)

## Description

RLDP config in check state

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:24|RESERVED||
|23:8|PERIOD|Interval between two retries in checking state(Unit: ms)|
|7:0|CNT|Number of re-send Loop Detection Packet in checking state|
