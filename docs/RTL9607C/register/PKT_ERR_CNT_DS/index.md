---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: PKT_ERR_CNT_DS

## Details

*Name* PKT_ERR_CNT_DS

*Offset* 0xF0C014

*Feature* [PONNIC_CTRL](../../feature/PONNIC_CTRL)

## Description

PONNIC packet counters for PBO downstream

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|TX_ERR_CNT|packet counter of Tx errors including Tx abort, carrier lost and out of window collision|
|15:0|RX_ERR_CNT|packet counter of Rx errors including CRC error packets (should be larger than 8 bytes) and missed packets|
