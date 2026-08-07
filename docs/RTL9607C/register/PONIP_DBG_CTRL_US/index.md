---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: PONIP_DBG_CTRL_US

## Details

*Name* PONIP_DBG_CTRL_US

*Offset* 0xF02930

*Feature* [PONIP_SCHEDULING_UPSTREAM](../../feature/PONIP_SCHEDULING_UPSTREAM)

## Description

PON flow control tuning debug control

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:19|RESERVED||
|18:11|CFG_US_EP_IPG|Set to 0xd by SDK for "Huawei 5680T 65 + 4n byte issue"|
|10|UNTAG_IFG_MODIFY||
|9|SIDCNT_ACC_BUSY|wait bit|
|8|CLR_SID_MAX_PAGE_CNT|set to trigger clear|
|7|RD_SID_MAX_PAGE_CNT|set to trigger read|
|6:0|SID_NO|PON port sid number|
