---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: RNG_CHK_PKTLEN_RNG

## Details

*Name* RNG_CHK_PKTLEN_RNG

*Offset* 0x15554

*Feature* [RANGE_CHECK_PORT_VLAN_IP_L4PORT_](../../feature/RANGE_CHECK_PORT_VLAN_IP_L4PORT_)

*Bit Offset:* 32

*Array Range:* 0-7

## Description

L4 packet length range check configuration.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:29|RESERVED||
|28|TYPE|Range checking data type<br>0x0:don’t revise the compare result<br>0x1:revise the compare result|
|27:14|PKTLEN_UPPER|Packet length upper bound.|
|13:0|PKTLEN_LOWER|Packet length lower bound.|
