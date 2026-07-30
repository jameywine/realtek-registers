---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: UNKN_IP4_MC

## Details

*Name* UNKN_IP4_MC

*Offset* 0x1C01C

*Feature* [ADDRESS_TABLE_LOOKUP](../../feature/ADDRESS_TABLE_LOOKUP)

*Bit Offset:* 2

*Port Range:* 0-10

## Description

unknow IPv4 multicast register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|1:0|ACT|unknow IPv4 multicast frame behavior<br>0b00: normal flooding<br>0b01: drop packet, exclude IP 224.0.0.x and IGMP packets<br>0b10: trap to CPU, exclude IP 224.0.0.x and IGMP packets<br>0b11: reserved|
