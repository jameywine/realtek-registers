---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: RLDP_LP_STS_CTRL

## Details

*Name* RLDP_LP_STS_CTRL

*Offset* 0x1A008

*Feature* [RLDP](../../feature/RLDP)

## Description

RLDP config in looped state

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:24|RESERVED||
|23:8|PERIOD|Interval between two retries in looped state(Unit: ms)|
|7:0|CNT|Number of re-send Loop Detection Packet in looped state|
