---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: IGMP_GLB_CTRL

## Details

*Name* IGMP_GLB_CTRL

*Offset* 0x11094

*Feature* [IGMP_SNOOPING](../../feature/IGMP_SNOOPING)

## Description

IGMP snooping global control

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:8|RESERVED||
|7:5|TRAP_PRIORITY|Specify the priority of trapped IGMP/MLD packets|
|4|PISO_LEAKY|Port isolation leaky for IGMP/MLD packets<br>1: Enable Leaky<br>0: Disable Leaky|
|3|VLAN_LEAKY|VLAN leaky for IGMP/MLD packets<br>1: Enable Leaky<br>0: Disable Leaky|
|2|DISC_STORM_FILTER|Discard packet flow counting in storm filtering control for IGMP/MLD packets<br>1: Discard strom counting<br>0: Enable Strom counting|
|1:0|RESERVED||
