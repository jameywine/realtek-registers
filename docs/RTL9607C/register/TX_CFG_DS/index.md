---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: TX_CFG_DS

## Details

*Name* TX_CFG_DS

*Offset* 0xF0C040

*Feature* [PONNIC_CTRL](../../feature/PONNIC_CTRL)

## Description

PONNIC Downstream Transmit Configuration Register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:13|RESERVED||
|12:10|IFG|InterFrameGap Time: This field allows the user to adjust the interframe gap time longer than the standard: 9.6 us for 10Mbps, 960 ns for 100Mbps. The time can be programmed from 9.6 us to 14.4 us (10Mbps) and 960ns to 1440ns (100Mbps).|
|9:4|RESERVED||
|3|R_TX_HPRI||
|2:1|R_PREAMBLE_LEN|Set to 1 by SDK during PBO init|
|0|R_TX_PADDING|Set by SDK during PBO init. Similar to CPU NIC's TC register bit 0?|
