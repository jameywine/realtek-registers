---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: STAT_RST

## Details

*Name* STAT_RST

*Offset* 0x34018

*Feature* [STATISTIC_COUNTERS](../../feature/STATISTIC_COUNTERS)

## Description

MIB reset register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:4|RESERVED||
|3|RST_STAT|ASIC is resetting MIB|
|2|RST_MIB_VAL|Reset MIB counter(except private debug counter ) to 0 or all 1<br>0b1: reset counter to all ’1’<br>0b0: reset counter to 0|
|1|RESERVED||
|0|RST_QM_MIB|Reset global MIB counters.<br>Write 1 to clear MIB counters. After resetting, the value is reset to 0|
