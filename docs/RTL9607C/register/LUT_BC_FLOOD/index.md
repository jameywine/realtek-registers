---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: LUT_BC_FLOOD

## Details

*Name* LUT_BC_FLOOD

*Offset* 0x1C028

*Feature* [ADDRESS_TABLE_LOOKUP](../../feature/ADDRESS_TABLE_LOOKUP)

*Bit Offset:* 1

*Port Range:* 0-10

## Description

LUT broadcast flooding control register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|0|EN|Egress port mask for broadcast(ff-ff-ff-ff-ff-ff) flooding packets<br>0b0: drop<br>0b1: normal flooding|
