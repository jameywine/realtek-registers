---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: UNKN_IP6_MC

## Details

*Name* UNKN_IP6_MC

*Offset* 0x1C020

*Feature* [ADDRESS_TABLE_LOOKUP](../../feature/ADDRESS_TABLE_LOOKUP)

*Bit Offset:* 2

*Port Range:* 0-10

## Description

unknow IPv6 multicast register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|1:0|ACT|unknow IPv6 multicast frame behavior<br>0b00: normal flooding<br>0b01: drop packet, exclude IP [FFXX::/8] and MLD packets<br>0b10: trap to CPU, exclude IP [FFXX::/8] and MLD packets<br>0b11: reserved|
