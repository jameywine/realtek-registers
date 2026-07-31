---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: RMA_CTRL_SSTP

## Details

*Name* RMA_CTRL_SSTP

*Offset* 0x1C10C

*Feature* [RMA](../../feature/RMA)

## Description

Cisco Shared Spanning Tree Protocol control register for 01-00-0C-CC-CC-CD

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:6|RESERVED||
|5:4|OPERATION|Operation setting for aware Reserved Multicast Address<br>0B00: forwarding<br>0B01: trap to CPU<br>0B10: drop<br>0B11: forward, but not trap to CPU|
|3|DISCARD_STORM_FILTER|Discard packet flow counting in storm filtering control for aware Reserved Multicast Address<br>0B0: disable<br>0B1: enable|
|2|KEEP_FORMAT|Keep packet C-tag format for aware Reserved Multicast Address<br>0B0: disable<br>0B1: enable|
|1|VLAN_LEAKY|Bypass CVLAN egress filtering for aware Reserved Multicast Address<br>0B0: disable<br>0B1: enable|
|0|PORTISO_LEAKY|Bypass port isolation function for aware Reserved Multicast Address<br>0B0: disable<br>0B1: enable|
