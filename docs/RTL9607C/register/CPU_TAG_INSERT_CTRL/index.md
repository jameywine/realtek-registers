---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: CPU_TAG_INSERT_CTRL

## Details

*Name* CPU_TAG_INSERT_CTRL

*Offset* 0x230F4

*Feature* [MAC_CONTROL](../../feature/MAC_CONTROL)

*Bit Offset:* 1

*Port Range:* 0-2

## Description

CPU tag insert control register
Port range is for CPU GMAC id
GMAC id of 0 is CPU port 9
GMAC id of 1 is CPU port 10
GMAC id of 2 is CPU port 7

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|0|EN|insert CPU tag for trap port<br>0b0: disable<br>0b1: enable|
