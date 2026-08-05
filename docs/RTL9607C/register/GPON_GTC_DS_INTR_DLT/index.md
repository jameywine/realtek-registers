---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GTC_DS_INTR_DLT

## Details

*Name* GPON_GTC_DS_INTR_DLT

*Offset* 0x701000

*Feature* [GTC_DOWNSTREAM](../../feature/GTC_DOWNSTREAM)

## Description

GTC downstream interrupt indicator

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15|GTC_DS_INTR|Interrupt status of GTC_DS page.<br>GTC_DS_INTR = (LOS_DLT and LOS_M) or<br>(LOF_DLT and LOF_M) or<br>(DS_FEC_STA_DLT and DS_FEC_STA_M) or<br>(LOM_DLT and LOM_M) or<br>(SN_REQ_HIS and SN_REQ_M) or<br>(RNG_REQ_HIS and RNG_REQ_M) or<br>(PLM_BUF_REQ and PLM_BUF_M)|
|14:12|RESERVED||
|11|PPS_DLT||
|10|PLM_BUF_REQ|When PLOAMd buffer is not empty, this bit is set to high.|
|9|RNG_REQ_HIS|One or more Ranging Request received since last time of reading.|
|8|SN_REQ_HIS|One or more SN Request received since last time of reading.|
|7:4|RESERVED||
|3|LOM_DLT|It indicates the Super-Frame status has changed since last time of reading.|
|2|DS_FEC_STA_DLT|It indicates the downstream FEC on/off status has changed since last time of reading.|
|1|LOF_DLT|It indicates the status of LOF has changed since last time of reading.|
|0|LOS_DLT|It indicates the status of LOS has changed since last time of reading.|
