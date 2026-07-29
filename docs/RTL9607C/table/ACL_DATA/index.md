---
tags:
  - RTL9607C
  - Table
  - Table Fields
---

# RTL9607C table: ACL_DATA

## Details

*Name* ACL_DATA

*Feature* [TABLE_ACCESS](../../feature/TABLE_ACCESS)

*Type* 2

*Entries* 128

*Control register* [TBL_ACCESS_CTRL](../../register/TBL_ACCESS_CTRL)

*Write Data register* [TBL_ACCESS_WR_DATA](../../register/TBL_ACCESS_WR_DATA)

*Read Data register* [TBL_ACCESS_RR_DATA](../../register/TBL_ACCESS_RR_DATA)

## Description

ACL rule data bits Table

## Fields

|Name|LSB|Bits|Description|
| :--- | :--- | :--- | :--- |
|VALID|144|1|Valid bit|
|FIELD7|128|16|field 7|
|FIELD6|112|16|field 6|
|FIELD5|96|16|field 5|
|FIELD4|80|16|field 4|
|FIELD3|64|16|field 3|
|FIELD2|48|16|field 2|
|FIELD1|32|16|field 1|
|FIELD0|16|16|field 0|
|PMSK|5|11|Active port mask|
|TAGS|3|2|care tags|
|TYPE|0|3|ACL template number|
