---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: VLAN_EXT_PPB_VLAN

## Details

*Name* VLAN_EXT_PPB_VLAN

*Offset* 0x13188

*Feature* [_IEEE802_1V_PROTOCOL_BASED_VLAN](../../feature/_IEEE802_1V_PROTOCOL_BASED_VLAN)

*Bit Offset:* 12

*Array Range:* 0-3

*Port Range:* 0-17

## Description

Per Extension port per-protocol specifies the Protocol-and-Port-based VLAN. A packet is given to the
specified VID if its protocol value hit the PPB configuration.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|11:0|VID|Protocol-and-Port-based VLAN|
