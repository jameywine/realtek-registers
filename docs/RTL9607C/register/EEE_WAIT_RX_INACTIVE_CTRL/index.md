---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: EEE_WAIT_RX_INACTIVE_CTRL

## Details

*Name* EEE_WAIT_RX_INACTIVE_CTRL

*Offset* 0x23138

*Feature* [POWER_SAVING](../../feature/POWER_SAVING)

## Description

monitor rxdv for specific time to decide if enter TX LPI

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:27|RESERVED||
|26|EEE_WAIT_RX_INACTIVE_2P5G|control if TX LPI decision must consider rxdv idle time for 2.5G|
|25|EEE_WAIT_RX_INACTIVE_GE|control if TX LPI decision must consider rxdv idle time for giga|
|24|EEE_WAIT_RX_INACTIVE_GELITE|control if TX LPI decision must consider rxdv idle time for 500M|
|23:16|EEE_WAIT_RX_INACTIVE_TIMER_2P5G|min rxdv idle time for 2.5G TX LPI enter condition|
|15:8|EEE_WAIT_RX_INACTIVE_TIMER_GE|min rxdv idle time for giga TX LPI enter condition|
|7:0|EEE_WAIT_RX_INACTIVE_TIMER_GELITE|min rxdv idle time for 500M TX LPI enter condition|
