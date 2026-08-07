---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: SW_PBO_SID_PAGE_CNT

## Details

*Name* SW_PBO_SID_PAGE_CNT

*Offset* 0xF120E4

*Feature* [SWPBO](../../feature/SWPBO)

## Description

switch PBO SID used page current and maximum counters.

Counters are populated after setting PONIP_SID_READ bit and selecting SID in the PONIP_SID_SEL bit field of SW_PBO_SCH_MISC register.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:26|RESERVED||
|25:16|MAX|SID max page counter|
|15:10|RESERVED||
|9:0|CURRENT|SID current page counter|
