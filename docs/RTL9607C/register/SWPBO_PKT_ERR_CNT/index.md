---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: SWPBO_PKT_ERR_CNT

## Details

*Name* SWPBO_PKT_ERR_CNT

*Offset* 0xF14014

*Feature* [SWPBO_NIC_CTRL](../../feature/SWPBO_NIC_CTRL)

## Description

PONNIC packet counters for Switch PBO

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|TX_ERR_CNT|packet counter of Rx errors including CRC error packets (should be larger than 8 bytes) and missed packets|
|15:0|RX_ERR_CNT|packet counter of Tx errors including Tx abort, carrier lost and out of window collision|
