---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: IGR_BWCTRL_P_CTRL

## Details

*Name* IGR_BWCTRL_P_CTRL

*Offset* 0x20010

*Feature* [BANDWIDTH_CONTROL_INGRESS_EGRESS_](../../feature/BANDWIDTH_CONTROL_INGRESS_EGRESS_)

*Bit Offset:* 32

*Port Range:* 0-10

## Description

Ingress bandwidth control per-port control register.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:21|RESERVED||
|20:2|RATE|Ingress Bandwidth Control, unit: 8Kbps (K=1024) 17’h7ffff : BW= full rate (line rate) N : BW=N*8Kbps|
|1|MODE|Flow control setting while input rate is over input bandwidth<br>0: disable, drop packet<br>1: enable flow control|
|0|IFG|Bandwidth Control Include/exclude Preamble & IFG (20bytes)<br>0: exclude<br>1: include|
