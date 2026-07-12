---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: P_ABLTY

## Details

*Name* P_ABLTY

*Offset* 0x200

*Feature* [CHP_INFORMATION](../../feature/CHP_INFORMATION)

*Bit Offset:* 32

*Port Range:* 0-10

## Description

MAC Port Ability Status

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15|EEE_ABLTY||
|14|RESERVED||
|13:12|SPEED_ABLTY23||
|11|LPI_1000||
|10|LPI_100||
|9|P_NWAY_FAULT|N-way fault|
|8|P_MSTR|link on in master mode|
|7|P_NWAY_ABLTY|Auto-Negotiation Ability|
|6|P_TX_FC|transmit flow control capable<br>0:not flow control capable<br>1:flow control capable|
|5|P_RX_FC|receive flow control capable<br>0:not flow control capable<br>1:flow control capable|
|4|P_LINK_STATUS|link status|
|3|P_LINK_FIB1G|link at fiber 1g|
|2|P_DUPLEX|full duplex capable<br>0=half duplex<br>1=full duplex|
|1:0|P_LINK_SPD|link speed.<br>00=10M<br>01=100M<br>10=1000M|
