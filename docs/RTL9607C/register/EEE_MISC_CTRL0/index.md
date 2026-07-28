---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: EEE_MISC_CTRL0

## Details

*Name* EEE_MISC_CTRL0

*Offset* 0x2312C

*Feature* [POWER_SAVING](../../feature/POWER_SAVING)

## Description

EEE Miscellaneous Control 0

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:5|RESERVED||
|4|EEE_EN_FC_EFCT|Enable EEE Flow control Effect? |
|3|EEE_REF_RXLPI|Enable LPI RX Reference?|
|2:1|EEE_LINK_UP_DELAY|Linkup delay value?|
|0|EEE_TX_WAKE_SEL|Select LPI TX wake up decision mode for EEE.<br>0b0: wake up when any packet is going to TX.<br>0b1: wake up when a high priority packet is going to TX or queued enough low priority packets (more than LOW_Q_THR) or low priority packets waiting enough time (more than TX_DELAY_TIMER_100M/ TX_DELAY_TIMER_GIGA) in queue.|
