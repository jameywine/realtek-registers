---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: FORCE_P_ABLTY

## Details

*Name* FORCE_P_ABLTY

*Offset* 0x1CC

*Feature* [CHP_INFORMATION](../../feature/CHP_INFORMATION)

*Bit Offset:* 32

*Port Range:* 0-10

## Description

MAC Force Port Ability

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15|EEE_ABLTY||
|14|RESERVED||
|13:12|SPEED23_ABLTY||
|11|LPI_1000_ABLTY||
|10|LPI_100_ABLTY||
|9|MST_FAULT_ABLTY|N-way fault|
|8|MST_MOD_ABLTY|link on in master mode|
|7|NWAY_ABLTY|Auto-Negotiation Ability|
|6|TXPAUSE_ABLTY|transmit flow control capable<br>0:not flow control capable<br>1:flow control capable|
|5|RXPAUSE_ABLTY|receive flow control capable<br>0:not flow control capable<br>1:flow control capable|
|4|LINK_ABLTY|link status|
|3|FIB1G_ABLTY|link at fiber 1g|
|2|DUPLEX_ABLTY|full duplex capable<br>0=half duplex<br>1=full duplex|
|1:0|SPEED01_ABLTY|link speed.<br>00=10M<br>01=100M<br>10=1000M|
