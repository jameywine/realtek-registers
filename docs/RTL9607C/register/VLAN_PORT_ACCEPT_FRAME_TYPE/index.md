---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: VLAN_PORT_ACCEPT_FRAME_TYPE

## Details

*Name* VLAN_PORT_ACCEPT_FRAME_TYPE

*Offset* 0x13000

*Feature* [_IEEE802_1Q_VLAN](../../feature/_IEEE802_1Q_VLAN)

*Bit Offset:* 2

*Port Range:* 0-10

## Description

VLAN accept frame type per port configuration.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|1:0|FRAME_TYPE|0b00: Admit All frames<br>0b01: Admit Only VLAN-tagged frames(VID 0-4094 and VID 4095 if VLAN_VID4095_TYPE = 1 and VLAN_VID0_TYPE = 1)<br>0b10: Admit Only Untagged and Priority-tagged frames.(Also VID 4095 if VLAN_VID4095_TYPE = 0)<br>0b11: Admit 1Q and 1P tagged frame(VID 0 4095)|
