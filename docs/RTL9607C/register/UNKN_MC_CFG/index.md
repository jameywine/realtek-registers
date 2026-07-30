---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: UNKN_MC_CFG

## Details

*Name* UNKN_MC_CFG

*Offset* 0x1C024

*Feature* [ADDRESS_TABLE_LOOKUP](../../feature/ADDRESS_TABLE_LOOKUP)

## Description

unknow multicast configuration register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:15|RESERVED||
|14|UNKN_MC_DHCP6_TRAP|unknown multicast DHCPv6 packet trap action.<br>0: Disable.<br>1: Enable.|
|13|UNKN_MC_ICMP6_TRAP|unknown multicast ICMPv6 packet trap action.<br>0: Disable.<br>1: Enable.|
|12:7|UNKN_MC_IP6_RSV_ADDR|dynamic address aging out configuration of the specified port.|
|6:5|UNKN_RSV_IP6_ACT|unknown Reserved IPv6 multicast address packet action.<br>0: treat as normal unknown multicast packet.<br>1: always flooding.<br>2: trap to CPU.|
|4:3|UNKN_RSV_IP4_ACT|unknown Reserved IPv4 multicast address packet action.<br>0: treat as normal unknown multicast packet.<br>1: always flooding.<br>2: trap to CPU.|
|2:0|UNKN_MC_PRI|Trap priority for unknown L2/Ipv4/IPv6 multicast|
