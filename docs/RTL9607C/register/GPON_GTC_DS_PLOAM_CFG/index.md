---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GTC_DS_PLOAM_CFG

## Details

*Name* GPON_GTC_DS_PLOAM_CFG

*Offset* 0x70101C

*Feature* [GTC_DOWNSTREAM](../../feature/GTC_DOWNSTREAM)

## Description

PLOAMd message configuration

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:11|RESERVED||
|10|PLM_DROP_CRCE|0x0: accept and buffer received PLOAMd messages with CRC error, for software to process/debug.<br>0x1: dropping received PLOAMd messages with CRC error. (counters will be increased)|
|9|PLM_BC_ACC_EN|0x0: Discard broadcast PLOAMd message.<br>0x1: Accept broadcast PLOAMd message.<br>Should be always set.|
|8|PLM_DS_ONUID_FLT_EN|0x0: Disable ONU_ID filter for downstream PLOAM.<br>0x1: Enable ONU_ID filter for downstream PLOAM.|
|7:0|PLM_DS_NOMSG_ID|Message ID of downstream NO_MSG PLOAM message.<br>Should always keep the default value. Here make it configurable just for debugging.|
