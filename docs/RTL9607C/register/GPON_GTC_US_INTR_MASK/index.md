---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GTC_US_INTR_MASK

## Details

*Name* GPON_GTC_US_INTR_MASK

*Offset* 0x705004

*Feature* [GTC_UPSTREAM](../../feature/GTC_UPSTREAM)

## Description

GTC upstream intrrupt mask

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:11|RESERVED||
|10|ALL_QUEUE_EMPTY_M||
|9|OPTIC_SD_MISM_M|0x0: Not generating interrupt when OPTIC_SD_MISM_DLT is set.<br>0x1: Enable OPTIC_SD_MISM_DLT to generating interrupt.|
|8|OPTIC_SD_TOOLONG_M|0x0: Not generating interrupt when OPTIC_SD_TOOLONG_DLT is set.<br>0x1: Enable OPTIC_SD_TOOLONG_DLT to generating interrupt.|
|7|PLM_NRM_EMPTY_M|0x0: Not generating interrupt when PLM_NRM_EMPTY_DLT is set.<br>0x1: Enable PLM_NRM_EMPTY_DLT to generating interrupt.|
|6|RESERVED||
|5|PLM_URG_EMPTY_M|0x0: Not generating interrupt when PLM_URG_EMPTY_DLT is set.<br>0x1: Enable PLM_URG_EMPTY_DLT to generating interrupt.|
|4:3|RESERVED||
|2|US_FEC_STS_M|0x0: Not generating interrupt when US_FEC_STA_DLT is set.<br>0x1: Enable US_FEC_STS_DLT to generating interrupt.|
|1|RESERVED||
|0|DG_MSG_TX_M|0x0: Not generating interrupt when DG_MSG_TX_IRQ is set.<br>0x1: Enable DG_MSG_TX_IRQ to generating interrupt.|
