---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: EGR_BWCTRL_P_CTRL

## Details

*Name* EGR_BWCTRL_P_CTRL

*Offset* 0x2D804

*Feature* [SCHEDULING](../../feature/SCHEDULING)

*Bit Offset:* 32

*Port Range:* 0-10

## Description

egress bandwidth control per-port control register.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:20|RESERVED||
|19:1|RATE|Egress Bandwidth Control, unit: 8Kbps (K=1024)<br>17’h1ffff : BW= full rate (line rate)<br>N : BW=N*8Kbps|
|0|IFG|Bandwidth Control Include/Exclude Preamble & IFG (20 bytes)<br>0: exclude<br>1: Include|
