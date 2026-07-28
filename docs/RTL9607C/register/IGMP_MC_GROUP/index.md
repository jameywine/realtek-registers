---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: IGMP_MC_GROUP

## Details

*Name* IGMP_MC_GROUP

*Offset* 0x1C2F0

*Feature* [IGMP_SNOOPING](../../feature/IGMP_SNOOPING)

*Bit Offset:* 64

*Array Range:* 0-63

## Description

Specify IP multicast group IP

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|63:54|RESERVED||
|53|VALID|Validity?|
|52:48|EXTMBRIDX|Forwarding extension portmask|
|47:43|RESERVED||
|42:32|PMSK|Forwarding portmask|
|31:28|RESERVED||
|27:0|GIP|GIP for IGMP snooping entry|
