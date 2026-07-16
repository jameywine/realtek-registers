---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: CPU_TAG_AWARE_CTRL

## Details

*Name* CPU_TAG_AWARE_CTRL

*Offset* 0x230F8

*Feature* [MAC_CONTROL](../../feature/MAC_CONTROL)

*Bit Offset:* 1

*Port Range:* 0-2

## Description

CPU tag aware control register
Port range is for CPU GMAC id
GMAC id of 0 is CPU port 9
GMAC id of 1 is CPU port 10
GMAC id of 2 is CPU port 7

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|0|EN|CPU tag ingress parsering aware port<br>0b1:enable|
