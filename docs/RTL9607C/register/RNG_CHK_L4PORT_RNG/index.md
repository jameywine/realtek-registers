---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: RNG_CHK_L4PORT_RNG

## Details

*Name* RNG_CHK_L4PORT_RNG

*Offset* 0x154D4

*Feature* [RANGE_CHECK_PORT_VLAN_IP_L4PORT_](../../feature/RANGE_CHECK_PORT_VLAN_IP_L4PORT_)

*Bit Offset:* 64

*Array Range:* 0-15

## Description

L4 port range check configuration.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|63:34|RESERVED||
|33:32|TYPE|Range checking data type<br>0x0:non-valid<br>0x1:soruce port range check<br>0x2:destination range check<br>0x3:reserved|
|31:16|L4PORT_UPPER|TCP/UDP port upper bound.|
|15:0|L4PORT_LOWER|TCP/UDP port lower bound.|
