---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: VLAN_PPB_VLAN_VAL

## Details

*Name* VLAN_PPB_VLAN_VAL

*Offset* 0x130C8

*Feature* [_IEEE802_1V_PROTOCOL_BASED_VLAN](../../feature/_IEEE802_1V_PROTOCOL_BASED_VLAN)

*Bit Offset:* 32

*Array Range:* 0-3

## Description

Specify IEEE 802.1v(Protocol-and-Port-based VLAN) configuration. Global eight protocol val-
ues are supported and each port can have different PPB VLAN for the same protocol value through
VLAN_PORT_PPB_VLAN.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:18|RESERVED||
|17:2|ETHER_TYPE|EtherType or DSAP/SSAP of protocol and port based vlan|
|1:0|FRAME_TYPE|Frame format of protocol and port based vlan<br>0b00: Ethernet<br>0b01: LLC_Other<br>0b10: RFC1042<br>0b11:As usage disabled|
