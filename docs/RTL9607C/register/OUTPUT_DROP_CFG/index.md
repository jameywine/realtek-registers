---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: OUTPUT_DROP_CFG

## Details

*Name* OUTPUT_DROP_CFG

*Offset* 0x11088

*Feature* [SCHEDULING](../../feature/SCHEDULING)

## Description

Output drop configuration

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:3|RESERVED||
|2|OD_BC_SEL|Select broadcast packet type for output drop control<br>1: select<br>0: not select|
|1|OD_MC_SEL|Select multicast packet type for output drop control<br>1: select<br>0: not select|
|0|OD_UC_SEL|Select unknown unicast packet type for output drop control<br>1: select<br>0: not select|
