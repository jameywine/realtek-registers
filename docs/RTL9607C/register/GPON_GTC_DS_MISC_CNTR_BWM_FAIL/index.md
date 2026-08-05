---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GTC_DS_MISC_CNTR_BWM_FAIL

## Details

*Name* GPON_GTC_DS_MISC_CNTR_BWM_FAIL

*Offset* 0x7011A4

*Feature* [GTC_DOWNSTREAM](../../feature/GTC_DOWNSTREAM)

## Description

Dowmstream statistics.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|CNTR_BWMAP_OVERFLOW|Number of BWMap items dropped due to BWMap buffering limitation (32 items per GPON frame).|
|15:0|CNTR_BWMAP_CRC_ERR|Number of BWMap items dropped due to CRC error.|
