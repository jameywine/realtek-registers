---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: SW_PBO_SCH_MISC

## Details

*Name* SW_PBO_SCH_MISC

*Offset* 0xF120F0

*Feature* [SWPBO](../../feature/SWPBO)

## Description

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:10|RESERVED||
|9|SWPBOQ_EN||
|8|PONIP_SID_MAX_PG_CLR|Set to clear SID max page counter|
|7|PONIP_SID_BUSY|Busy bit?|
|6|PONIP_SID_READ|Set to perform a read operation to get counter stats.|
|5:0|PONIP_SID_SEL|PON SID select to read the counters from. Calculated by the equation "port_num * 8 + queue_num"|
