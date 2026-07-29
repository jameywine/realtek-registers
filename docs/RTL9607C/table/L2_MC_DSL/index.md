---
tags:
  - RTL9607C
  - Table
  - Table Fields
---

# RTL9607C table: L2_MC_DSL

## Details

*Name* L2_MC_DSL

*Feature* [TABLE_ACCESS](../../feature/TABLE_ACCESS)

*Type* 0

*Entries* 2112

*Control register* [TBL_ACCESS_CTRL](../../register/TBL_ACCESS_CTRL)

*Write Data register* [TBL_ACCESS_WR_DATA](../../register/TBL_ACCESS_WR_DATA)

*Read Data register* [TBL_ACCESS_RR_DATA](../../register/TBL_ACCESS_RR_DATA)

## Description

L2 Table (Multicast)

## Fields

|Name|LSB|Bits|Description|
| :--- | :--- | :--- | :--- |
|VALID|79|1|CAM valid bit|
|EXT_MBRIDX|74|5|extension port member index|
|MBR|63|11|port member|
|IVL_SVL|62|1|IVL=1 or SVL=0|
|NOT_SALEARN|61|1|ASIC auto SA learning indicator<br>0:ASIC auto learning|
|L3LOOKUP|60|1|IP Multicast<br>0b0: Non IP multicast entry<br>0b1: IP multicast entry|
|VID_FID|48|12|12-bits VID for IVL<br>4-bits FID for SVL|
|MAC|0|48|MAC address|
