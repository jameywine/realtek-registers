---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: SVLAN_CTRL

## Details

*Name* SVLAN_CTRL

*Offset* 0x1403C

*Feature* [_IEEE802_1AD_PROVIDER_BRIDGES_Q_IN_Q](../../feature/_IEEE802_1AD_PROVIDER_BRIDGES_Q_IN_Q)

## Description

SVLAN related control register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:28|RESERVED||
|27|VS_FILTERING||
|26:22|RESERVED||
|21|VS_DEI_KEEP|Keep SVLAN ingress tag DEI<br>0b0: Always egress DEI=0<br>0b1: Keep ingress tag DEI value to egress tag|
|20:18|VS_PRI|Trap priority for SVLAN trapping packets|
|17:4|RESERVED||
|3:2|VS_UNTAG|un-stagged packet with trap to CPU action<br>0b00:drop<br>0b01: trap to CPU<br>0b10: assign ingress SVID VS_UNTAG_SVIDX<br>0b11: reserved|
|1:0|VS_SPRISEL|S-priority assignment of upstream packet setting<br>0b00: use internal priority<br>0b01: use 1Q tag priority<br>0b10: use VS_SPRI as S-Priority<br>0b11: using port based priority|
