---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: STAT_CTRL

## Details

*Name* STAT_CTRL

*Offset* 0x34000

*Feature* [STATISTIC_COUNTERS](../../feature/STATISTIC_COUNTERS)

## Description

MIB control register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:11|RESERVED||
|10|SYNC_STATUS|MIB stop sync status<br>0b0:Busy<br>0b1:Done|
|9:2|LATCH_TIMER|MIB latch timer, unit 1 second. Clear by asic atfer reach latch time|
|1|SYNC_MODE|MIB register data update mode<br>0b0: stop sync<br>0b1: normal free run sync|
|0|CNTING_MODE|MIB data update mode<br>0b00: normal free run counting<br>0b01: counting and latch all MIBs by MIB_TIMER control|
