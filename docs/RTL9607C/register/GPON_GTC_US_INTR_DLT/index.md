---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GTC_US_INTR_DLT

## Details

*Name* GPON_GTC_US_INTR_DLT

*Offset* 0x705000

*Feature* [GTC_UPSTREAM](../../feature/GTC_UPSTREAM)

## Description

GTC upstream intrrupt indicator

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15|GTC_US_INTR|Interrupt status of GTC_US page.<br>GTC_US_INTR = (US_FEC_STA_DLT and US_FEC_STA_M) or (PLM_URG_EMPTY_DLT and PLM_URG_EMPTY_M) or (PLM_NRM_EMPTY_DLT and PLM_NRM_EMPTY_M);|
|14:11|RESERVED||
|10|ALL_QUEUE_EMPTY_DLT||
|9|OPTIC_SD_MISM_DLT|0x1: upstream optic SD mis-matches with the GPON MAC output Burst Enable signal. The ONT is suspicious of a rogue ONT|
|8|OPTIC_SD_TOOLONG_DLT|0x1: upstream optic SD is asserted for too long time. The ONT is suspicious of a rogue ONT.|
|7|PLM_NRM_EMPTY_DLT|0x1: PLM_NRM_EMPTY changed to 0x0 since last time reading this address.|
|6|RESERVED||
|5|PLM_URG_EMPTY_DLT|0x1: PLM_URG_EMPTY changed to 0x0 since last time reading this address.|
|4:3|RESERVED||
|2|US_FEC_STS_DLT|0x1: US_FEC_STS changed since last time reading this address.|
|1|RESERVED||
|0|DG_MSG_TX_DLT|0x1: counter of transmitted Dying Gasp MSG reaching the DG_MSG_TX_CNT_THRESHOLD.<br>This bit cannot be cleared!|
