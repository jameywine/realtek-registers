---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: VLAN_CTRL

## Details

*Name* VLAN_CTRL

*Offset* 0x13008

*Feature* [_IEEE802_1Q_VLAN](../../feature/_IEEE802_1Q_VLAN)

## Description

VLAN global configuration.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:5|RESERVED||
|4|VID_4095_TYPE|0b0: treat VID 4095 as un-tagging frame<br>0b1: treat VID 4095 as tagging frame|
|3|VID_0_TYPE|0b0: treat VID 0 as un-tagging frame<br>0b1: treat VID 0 as tagging frame|
|2|CFI_KEEP|Keep ingress tag CFI<br>0b0: Always egress CFI=0<br>0b1: Keep ingress tag CFI value to egress tag|
|1|RESERVED||
|0|VLAN_FILTERING|VLAN ingress and egress filtering enable setting<br>0b0:disable<br>0b1:enable|
