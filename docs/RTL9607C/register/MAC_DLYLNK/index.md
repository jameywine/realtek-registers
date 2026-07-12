---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: MAC_DLYLNK

## Details

*Name* MAC_DLYLNK

*Offset* 0x2B4

*Feature* [CHP_INFORMATION](../../feature/CHP_INFORMATION)

## Description

SWCORE MAC delay link

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:17|RESERVED||
|16:15|LNKUP_DELAY_2P5G||
|14|LNKDN_FRC_DIS||
|13:6|TX_IDLE_TMR||
|5|MACRX_DUPDET_EN|Enable MAC RX Duplex Delay?|
|4|MAC_LNKUP_DELAY_EN|Enable MAC delay link up 2’b00 - disable delay link for gig|
|3:2|LNKUP_DELAY_GE_100M|2’b00 - disable delay link for giga and 100M 2’b01 - delay link for 10ms 2’b10 - delay link for 20ms 2’b11 - delay link for 30ms|
|1:0|LNKUP_DELAY_10M|2’b00 - delay link for 50ms 2’b01 - delay link for 150ms 2’b10 - delay link for 250ms 2’b11 - delay link for 350ms|
