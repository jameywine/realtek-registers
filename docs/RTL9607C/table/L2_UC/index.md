---
tags:
  - RTL9607C
  - Table
  - Table Fields
---

# RTL9607C table: L2_UC

## Details

*Name* L2_UC

*Feature* [TABLE_ACCESS](../../feature/TABLE_ACCESS)

*Type* 0

*Entries* 2112

*Control register* [TBL_ACCESS_CTRL](../../register/TBL_ACCESS_CTRL)

*Write Data register* [TBL_ACCESS_WR_DATA](../../register/TBL_ACCESS_WR_DATA)

*Read Data register* [TBL_ACCESS_RR_DATA](../../register/TBL_ACCESS_RR_DATA)

## Description

L2 Table (Unicast)

## Fields

|Name|LSB|Bits|Description|
| :--- | :--- | :--- | :--- |
|VALID|79|1|valid bit|
|EXT_SPA|76|3|EXT source port address|
|ARP_USAGE|75|1|ARP uage|
|DA_BLK|74|1|DA block|
|SA_BLK|73|1|SA block|
|AGE|70|3|Aging time|
|SPA|66|4|source port address|
|CTAG_IF|65|1||
|FID|63|2|FID|
|IVL_SVL|62|1|IVL=1 or SVL=0|
|NOT_SALEARN|61|1|ASIC auto SA learning indicator<br>0:ASIC auto learning|
|L3LOOKUP|60|1|IP Multicast<br>0b0: Non IP multicast entry<br>0b1: IP multicast entry|
|CVID|48|12|VID|
|MAC|0|48|MAC address|
