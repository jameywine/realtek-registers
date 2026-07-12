---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: ABLTY_FORCE_MODE

## Details

*Name* ABLTY_FORCE_MODE

*Offset* 0x238

*Feature* [CHP_INFORMATION](../../feature/CHP_INFORMATION)

*Bit Offset:* 32

*Port Range:* 0-10

## Description

MAC Force Port Ability State.
Set to 0xfff for CPU ports.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15|FORCE_EEE_ABLTY||
|14|RESERVED||
|13|FORCE_SPEED3_ABLTY||
|12|FORCE_SPEED2_ABLTY||
|11|FORCE_LPI_1000_ABLTY||
|10|FORCE_LPI_100_ABLTY||
|9|FORCE_MST_FAULT_ABLTY||
|8|FORCE_MST_MOD_ABLTY||
|7|FORCE_NWAY_ABLTY||
|6|FORCE_TXPAUSE_ABLTY||
|5|FORCE_RXPAUSE_ABLTY||
|4|FORCE_LINK_ABLTY||
|3|FORCE_FIB1G_ABLTY||
|2|FORCE_DUPLEX_ABLTY||
|1|FORCE_SPEED1_ABLTY||
|0|FORCE_SPEED0_ABLTY||
