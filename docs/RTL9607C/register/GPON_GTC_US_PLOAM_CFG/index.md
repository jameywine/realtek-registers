---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GTC_US_PLOAM_CFG

## Details

*Name* GPON_GTC_US_PLOAM_CFG

*Offset* 0x705100

*Feature* [GTC_UPSTREAM](../../feature/GTC_UPSTREAM)

## Description

PLOAMu configuration

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:5|RESERVED||
|4|PLM_FLUSH_BUF|Writing 0 then 1 to this bit to flush the PLOAM Tx buffer.<br>Better to flush buffer before entering O5.<br>SNmsg, NOmsg and DGmsg will not be impacted.|
|3:2|RESERVED||
|1|PLM_US_CRC_GEN_EN|0x1: GPON_MAC will generate CRC byte and override the original last byte.|
|0|PLM_US_ONUID_OVRD_EN|0x1: GPON_MAC will override the ONU_ID field in PLOAMu.|
