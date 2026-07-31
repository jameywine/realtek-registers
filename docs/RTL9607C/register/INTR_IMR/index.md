---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: INTR_IMR

## Details

*Name* INTR_IMR

*Offset* 0x1D00C

*Feature* [INTERRUPT](../../feature/INTERRUPT)

## Description

Switch interrupt mask register.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:21|RESERVED||
|20|IMR_TOD_UPDATE||
|19|IMR_SFP||
|18|IMR_TOD||
|17|IMR_FB||
|16|IMR_CRASH||
|15|IMR_SC||
|14|IMR_THERMAL_ALARM|IMR thermal alarm|
|13|IMR_DYING_GASP|IMR dying gasp|
|12|IMR_PTP_1_SEC|IMR PTP egress event|
|11|IMR_EPON|IMR EPON event|
|10|IMR_GPON|IMR GPON even|
|9|IMR_SERDES|IMR serdes interrupt|
|8|IMR_GPHY|IMR for GPHY interrupt|
|7|IMR_ACL|IMR for ACL interrupt|
|6|IMR_DBGO||
|5|IMR_LOOP|IMR for have loop detected or loop recoved situation happen|
|4|IMR_SPE_CONGEST|IMR for TX special congest|
|3|IMR_SPE_CHG|MR for speed change|
|2|IMR_L2_LRN_OVER|IMR for L2 learn over|
|1|IMR_METER_EXCEED|IMR for meter exceed|
|0|IMR_LINK_CHG|IMR for link change|
