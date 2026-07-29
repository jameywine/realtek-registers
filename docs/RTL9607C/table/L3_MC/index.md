---
tags:
  - RTL9607C
  - Table
  - Table Fields
---

# RTL9607C table: L3_MC

## Details

*Name* L3_MC

*Feature* [TABLE_ACCESS](../../feature/TABLE_ACCESS)

*Type* 0

*Entries* 2112

*Control register* [TBL_ACCESS_CTRL](../../register/TBL_ACCESS_CTRL)

*Write Data register* [TBL_ACCESS_WR_DATA](../../register/TBL_ACCESS_WR_DATA)

*Read Data register* [TBL_ACCESS_RR_DATA](../../register/TBL_ACCESS_RR_DATA)

## Description

L3 Table (Multicast)

## Fields

|Name|LSB|Bits|Description|
| :--- | :--- | :--- | :--- |
|VALID|79|1|valid bit|
|EXT_MBRIDX|74|5|extension port member index|
|MBR|63|11|port member|
|IVL_SVL|62|1||
|NOT_SALEARN|61|1|ASIC auto SA learning indicator<br>0:ASIC auto learning|
|L3LOOKUP|60|1|IP Multicast<br>0b0: Non IP multicast entry<br>0b1: IP multicast entry|
|SIP|28|32|Source IP address|
|GIP|0|28|Group IP address|
