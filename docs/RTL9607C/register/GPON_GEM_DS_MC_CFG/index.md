---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GEM_DS_MC_CFG

## Details

*Name* GPON_GEM_DS_MC_CFG

*Offset* 0x704080

*Feature* [GEM_PORT_DOWNSTREAM](../../feature/GEM_PORT_DOWNSTREAM)

## Description

Downstream GEM block multicast filtering configuration

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:11|RESERVED||
|10|IPV6_MC_FORCE_PASS|0x1: Always pass through IPv6 multicast frames.|
|9|IPV6_MC_FORCE_DROP|0x1: Always drop through IPv6 multicast frames, when IPv4_MC_FORCE_PASS = 0.|
|8:7|RESERVED||
|6|BROADCAST_PASS|0x1: Forward broadcast packets, i.e., bypass multicast filtering for broadcast packets.|
|5|RESERVED||
|4|NON_MULTICAST_PASS|0x0: Drop received non-broadcast frames which are neither IPv4 or IPv6 multicast frames<br>0x1: Pass received non-broadcast frames which are neither IPv4 or IPv6 multicast frames|
|3|FCS_CHK_EN|0x0: Disable FCS check.<br>0x1: Enable FCS check.|
|2|IPV4_MC_FORCE_PASS|0x1: Always pass through IPv4 multicast frames.|
|1|IPV4_MC_FORCE_DROP|0x1: Always drop through IPv4 multicast frames, when IPv4_MC_FORCE_PASS = 0.|
|0|MC_EXCL_MODE|0x1: Multicast filtering works in Excluding mode.<br>By default its 0x0: inclusive mode.|
