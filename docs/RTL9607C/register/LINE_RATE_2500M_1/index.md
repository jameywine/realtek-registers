---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: LINE_RATE_2500M_1

## Details

*Name* LINE_RATE_2500M_1

*Offset* 0x2D970

*Feature* [SCHEDULING](../../feature/SCHEDULING)

## Description

Line rate for 2.5Gbps Serdes 1

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:20|RESERVED||
|19|EN_RATE_2500M|Enable Line rate for 2.5G 1?|
|18:0|RATE|2.5G line rate control, unit: 8Kbps (K=1024)<br>N : BW=N*8Kbps|
