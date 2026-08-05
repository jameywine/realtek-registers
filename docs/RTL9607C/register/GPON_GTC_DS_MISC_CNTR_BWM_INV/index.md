---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GTC_DS_MISC_CNTR_BWM_INV

## Details

*Name* GPON_GTC_DS_MISC_CNTR_BWM_INV

*Offset* 0x7011A8

*Feature* [GTC_DOWNSTREAM](../../feature/GTC_DOWNSTREAM)

## Description

Dowmstream statistics.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|CNTR_BWMAP_INV1|Number of BWMap items dropped due to Sstop > 19439.|
|15:0|CNTR_BWMAP_INV0|Number of BWMap items dropped due to SStop < Sstart.|
