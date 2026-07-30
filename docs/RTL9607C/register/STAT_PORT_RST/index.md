---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: STAT_PORT_RST

## Details

*Name* STAT_PORT_RST

*Offset* 0x34014

*Feature* [STATISTIC_COUNTERS](../../feature/STATISTIC_COUNTERS)

*Bit Offset:* 1

*Port Range:* 0-11

## Description

Reset all of MIB counter for a specifed port.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|0|RST_PORT_MIB|Reset MIB counters for a port.<br>Write 1 to clear MIB counters. After resetting, the value is reset to 0|
