---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: PONIP_SID_USED_PAGE_CNT_US

## Details

*Name* PONIP_SID_USED_PAGE_CNT_US

*Offset* 0xF02938

*Feature* [PONIP_SCHEDULING_UPSTREAM](../../feature/PONIP_SCHEDULING_UPSTREAM)

## Description

PONIP used/max page counters

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:29|RESERVED||
|28:16|MAX_PAGE_CNT|Max Page Counter. Needs a read operation from PONIP_DBG_CTRL_US to retrieve the value.|
|15:13|RESERVED||
|12:0|USED_PAGE_CNT|Used Page Counter. Needs a read operation from PONIP_DBG_CTRL_US to retrieve the value.|
