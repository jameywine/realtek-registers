---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: TBL_ACCESS_CTRL

## Details

*Name* TBL_ACCESS_CTRL

*Offset* 0x12000

*Feature* [TABLE_ACCESS](../../feature/TABLE_ACCESS)

## Description

Table Access Control register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31|ACS_CMD_PS||
|30:24|RESERVED||
|23:12|ADDR|Access address for table access<br>(1)L2 access, 4-way hash imply each hash address contain 4 entry, the access address = {1’b0, hash address[8:0], entry[1:0]}.<br>L2 access also include BCAM, BCAM contain 64 entry, the access address = {1’b1, 5’b0, entry bits 5 0}|
|11:8|SPA|Port number for get next address|
|7:5|ACCESS_METHOD|Lut access method<br>0b000: with specify MAC/IP(read/write)<br>0b001: with specify lut address(read/write)<br>0b010: with specify next lut address(read)<br>0b011: with specify next lut address (only L2 UC entry, read)<br>0b100: with specify next lut address (only L2 MC entry, read)<br>0b101: with specify next lut address (only L3 MC entry, read)<br>0b110: with specify next lut address (only L2+L3 MC entry, read)<br>0b111: with specify next lut address (only L2 UC + SPA match entry, read)|
|4:3|CMD_TYPE|Table Read/Write/Reset type<br>0b00:read<br>0b01:write<br>0b10:reset|
|2:0|TBL_TYPE|table access select type (see below table)<br>0: LUT<br>1: CVLAN<br>2: ACL<br>3: ACL ACT<br>4: Classification(128 entries)<br>5: Classification Action(512 entries)|

## Control tables


|Name|Type|Summary|
| :--- | :--- | :--- |
|L2_MC_DSL|0|L2 Table (Multicast)|
|L2_UC|0|L2 Table (Unicast)|
|L3_MC|0|L3 Table (Multicast)|
|L3_MC_FID|0||
|L3_MC_VID|0||
|VLAN|1|VLAN Table|
|ACL_DATA|2|ACL rule data bits Table|
|ACL_MASK|2|ACL rule mask bits Table|
|ACL_ACTION_TABLE|3|ACL action Table|
|CF_MASK_T0|4|Classification rule mask table 0|
|CF_MASK_T1|4|Classification rule mask table 1|
|CF_MASK_T2|4|Classification rule mask table 2|
|CF_RULE_T0|4|Classification rule data table 0|
|CF_RULE_T1|4|Classification rule data table 1|
|CF_RULE_T2|4|Classification rule data table 2|
|CF_ACTION_DS|5|Classification downstrean action control table|
|CF_ACTION_US|5|Classification upstrean action control table|
