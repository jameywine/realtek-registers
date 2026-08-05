---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GEM_US_INTR_DLT

## Details

*Name* GPON_GEM_US_INTR_DLT

*Offset* 0x706000

*Feature* [GEM_UPSTREAM](../../feature/GEM_UPSTREAM)

## Description

GEM upstream intrrupt indicator

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31|GEM_US_INTR|Interrupt status of GEM_US page.|
|30:10|RESERVED||
|9|SD_VALID_LONG_DLT|0x1: SD_VALID_LONG_DLT changed to 0x0 since last time reading this address.|
|8|SD_DIFF_HUGE_DLT|0x1: SD_DIFF_HUGE_DLT changed to 0x0 since last time reading this address.|
|7|REQUEST_DELAY_DLT|0x1: REQUEST_DELAY_DLT changed to 0x0 since last time reading this address.|
|6|BC_LESS6_DLT|0x1: BC_LESS6_DLT changed to 0x0 since last time reading this address.|
|5|ERR_PLI_DLT|0x1: ERR_PLI_DLT changed to 0x0 since last time reading this address.|
|4|BURST_TM_LARGER_GTC_DLT|0x1: BURST_TM_LARGER_GTC_DLT changed since last time reading this address.|
|3|BANK_TOO_MUCH_AT_END_DLT|0x1: BANK_TOO_MUCH_AT_END_DLT changed since last time of reading this address.|
|2|BANK_REMAIN_AFRD_DLT|0x1: BANK_REMAIN_AFRD_DLT changed since last time reading this address.|
|1|BANK_OVERFL_DLT|0x1: BANK_OVERFL_IND changed since last time reading this address.|
|0|BANK_UNDERFL_DLT|0x1: BANK_UNDERFL_IND changed since last time reading this address.|
