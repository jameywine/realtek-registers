---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GEM_US_INTR_MASK

## Details

*Name* GPON_GEM_US_INTR_MASK

*Offset* 0x706004

*Feature* [GEM_UPSTREAM](../../feature/GEM_UPSTREAM)

## Description

GEM upstream intrrupt mask

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:10|RESERVED||
|9|SD_VALID_LONG_M|0x0: Disable SD_VALID_LONG_DLT from generating interrupt.<br>0x1: Enable SD_VALID_LONG_DLT to generating interrupt.|
|8|SD_DIFF_HUGE_M|0x0: Disable SD_DIFF_HUGE_DLT from generating interrupt.<br>0x1: Enable SD_DIFF_HUGE_DLT to generating interrupt.|
|7|REQUEST_DELAY_M|0x0: Disable REQUEST_DELAY_DLT from generating interrupt.<br>0x1: Enable REQUEST_DELAY_DLT to generating interrupt.|
|6|BC_LESS6_M|0x0: Disable BC_LESS6_DLT from generating interrupt.<br>0x1: Enable BC_LESS6_DLT to generating interrupt.|
|5|ERR_PLI_M|0x0: Disable ERR_PLI_DLT from generating interrupt.<br>0x1: Enable ERR_PLI_DLT to generating interrupt.|
|4|BURST_TM_LARGER_GTC_M|0x0: Disable BURST_TM_LARGER_GTC_DLT from generating interrupt.<br>0x1: Enable BURST_TM_LARGER_GTC_DLT to generating interrupt.|
|3|BANK_TOO_MUCH_AT_END_M|0x0: Disable BANK_TOO_MUCH_AT_END_DLTfrom generating interrupt.<br>0x1: Enable BANK_TOO_MUCH_AT_END_DLT to generating interrupt.|
|2|BANK_REMAIN_AFRD_M|0x0: Disable BANK_REMAIN_AFRD_DLT from generating interrupt.<br>0x1: Enable BANK_REMAIN_AFRD_DLT to generating interrupt.|
|1|BANK_OVERFL_M|0x0: Disable BANK_OVERFL_DLT from generating interrupt.<br>0x1: Enable BANK_OVERFL_DLT to generating interrupt.|
|0|BANK_UNDERFL_M|0x0: Disable BANK_UNDERFL_DLT from generating interrupt.<br>0x1: Enable BANK_UNDERFL_DLT to generating interrupt.|
