---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: VLAN_EGRESS_TAG

## Details

*Name* VLAN_EGRESS_TAG

*Offset* 0x2A000

*Feature* [_IEEE802_1Q_VLAN](../../feature/_IEEE802_1Q_VLAN)

*Bit Offset:* 32

*Port Range:* 0-10

## Description

VLAN tag egress format

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:2|RESERVED||
|1:0|EGRESS_MODE|Per-port VLAN tag egress format<br>0b00: Original mode. Output frame will follow VLAN untag setting.<br>0b01: Keep format mode. Output frame will keep VLAN original format.<br>0b10: Priority tag mode. Output frame will be priority tag.<br>0b11: Keep format mode. Output frame will keep VLAN original format.(the same as 0b01)|
