---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: EEE_TX_TIMER_100M_CTRL

## Details

*Name* EEE_TX_TIMER_100M_CTRL

*Offset* 0x2313C

*Feature* [POWER_SAVING](../../feature/POWER_SAVING)

## Description

Configure MAC 100M EEE timers containing rate calculation timer interval, delay timer for low queue packets to TX and wake up delay timer for leaving TX LPI mode.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:20|RESERVED||
|19:8|EEE_LOW_Q_TX_DELAY_FE|Timer value in EEE function to delay low queue packets to TX for 100M. A timer starts to count when a low queue packet reaches. When the timer is larger than TX_DELAY_TIMER_100M, the queued packets of the port would start to TX.<br>Unit: us.<br>Default value is 200 us for 100M.|
|7:0|EEE_TX_WAKE_TIMER_FE|Timer value in EEE function to wait before wake from LPI mode for 100M.<br>Value from 0 255.<br>Unit: us.<br>Default value is 36 us (0x24) for 100M.|
