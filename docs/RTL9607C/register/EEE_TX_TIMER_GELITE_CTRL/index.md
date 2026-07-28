---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: EEE_TX_TIMER_GELITE_CTRL

## Details

*Name* EEE_TX_TIMER_GELITE_CTRL

*Offset* 0x23140

*Feature* [POWER_SAVING](../../feature/POWER_SAVING)

## Description

Configure MAC 500M EEE timers containing rate calculation timer interval, delay timer for low queue packets to TX and wake up delay timer for leaving TX LPI mode.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:28|RESERVED||
|27:20|EEE_TX_PAUSE_WAKE_TIMER_GELITE|Delay timer for TX to wake up after sending out Pause frame?|
|19:8|EEE_LOW_Q_TX_DELAY_GELITE|Timer value in EEE function to delay low queue packets to TX for 500M. A timer starts to count when a low queue packet reaches. When the timer is larger than TX_DELAY_TIMER_500M, the queued packets of the port would start to TX.<br>Unit: us.<br>Default value is 200 us for 500M.|
|7:0|EEE_TX_WAKE_TIMER_GELITE|Timer value in EEE function to wait before wake from LPI mode for 500M.<br>Value from 0 255.<br>Unit: us.<br>Default value is 36 us for 500M.|
