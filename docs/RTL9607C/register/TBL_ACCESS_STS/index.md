---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: TBL_ACCESS_STS

## Details

*Name* TBL_ACCESS_STS

*Offset* 0x12004

*Feature* [TABLE_ACCESS](../../feature/TABLE_ACCESS)

## Description

Table Access Status register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:14|RESERVED||
|13|BUSY_FLAG|Busy Flag<br>0:Access operation is Done<br>1:Access operation is performing|
|12|HIT_STATUS|read or write with specify MAC status<br>0b0:unhit status, didn’t have such specify MAC entry in LUT<br>0b1:hit, have specify MAC entry already|
|11|TYPE|bcam or l2 address<br>0b0:L2 address<br>0b1:BCAM address|
|10:0|ADDR|Address|
