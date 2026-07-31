---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: INTR_IMS

## Details

*Name* INTR_IMS

*Offset* 0x1D010

*Feature* [INTERRUPT](../../feature/INTERRUPT)

## Description

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:21|RESERVED||
|20|IMS_TOD_UPDATE||
|19|IMS_SFP||
|18|IMS_TOD||
|17|IMS_FB||
|16|IMS_CRASH||
|15|IMS_SC||
|14|IMS_THERMAL_ALARM|IMS thermal alarm|
|13|IMS_DYING_GASP|IMS dying gasp|
|12|IMS_PTP_1_SEC|IMS PTP egress event|
|11|IMS_EPON|IMS EPON event|
|10|IMS_GPON|IMS GPON event|
|9|IMS_SERDES|IMS serdes interrupt|
|8|IMS_GPHY|IMS for GPHY interrupt|
|7|IMS_ACL|IMS for ACL interrup|
|6|IMS_DBGO|IMS for Cable Diag finish|
|5|IMS_LOOP|IMS for have loop detected or loop recoved situation happen|
|4|IMS_SPE_CONGEST|IMS for TX special congest|
|3|IMS_SPE_CHG|IMS for speed change|
|2|IMS_L2_LRN_OVER|IMS for L2 learn over|
|1|IMS_METER_EXCEED|IMS for meter exceed|
|0|IMS_LINK_CHG|IMS for link change|
