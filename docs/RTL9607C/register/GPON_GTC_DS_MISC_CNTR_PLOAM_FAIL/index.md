---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GTC_DS_MISC_CNTR_PLOAM_FAIL

## Details

*Name* GPON_GTC_DS_MISC_CNTR_PLOAM_FAIL

*Offset* 0x7011A0

*Feature* [GTC_DOWNSTREAM](../../feature/GTC_DOWNSTREAM)

## Description

Dowmstream statistics.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|CNTR_PLOAMD_OVERFLOW|Number of received PLOAMd messages dropped due to buffer overflow.|
|15:0|CNTR_PLOAMD_CRC_ERR|Number of PLOAMd messages with CRC error.|
