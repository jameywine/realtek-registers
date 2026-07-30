---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: MSTI_CTRL

## Details

*Name* MSTI_CTRL

*Offset* 0x1704C

*Feature* [SPANNING_TREE](../../feature/SPANNING_TREE)

*Bit Offset:* 2

*Array Range:* 0-3

*Port Range:* 0-10

## Description

MSTP Port State register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|1:0|STATE|Port status of multiple spanning tree<br>0b00: Disabled State<br>0b01: Blocking/Listening State<br>0b10: Learning State<br>0b11: Forwarding State|
