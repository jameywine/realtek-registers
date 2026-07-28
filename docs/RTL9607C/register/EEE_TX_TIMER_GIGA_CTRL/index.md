---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: EEE_TX_TIMER_GIGA_CTRL

## Details

*Name* EEE_TX_TIMER_GIGA_CTRL

*Offset* 0x23144

*Feature* [POWER_SAVING](../../feature/POWER_SAVING)

## Description

Configure MAC GIGA EEE timers containing rate calculation timer interval, delay timer for low queue packets to TX and wake up delay timer for leaving TX LPI mode.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:28|RESERVED||
|27:20|EEE_TX_PAUSE_WAKE_TIMER_GE|Delay timer for TX to wake up after sending out Pause frame?|
|19:8|EEE_LOW_Q_TX_DELAY_GE|Timer value in EEE function to delay low queue packets to TX for GIGA. A timer starts to count when a low queue packet reaches. When the timer is larger than TX_DELAY_TIMER_GIGA, the queued packets of the port would start to TX.<br>Unit: us.<br>Default value is 20 us for GIGA.|
|7:0|EEE_TX_WAKE_TIMER_GE|Timer value in EEE function to wait before wake from LPI mode for Giga.<br>Value from 0 255.<br>Unit: us.<br>Default value is 20 us for Giga.|
