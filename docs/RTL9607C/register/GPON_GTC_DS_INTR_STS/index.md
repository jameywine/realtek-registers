---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GTC_DS_INTR_STS

## Details

*Name* GPON_GTC_DS_INTR_STS

*Offset* 0x701008

*Feature* [GTC_DOWNSTREAM](../../feature/GTC_DOWNSTREAM)

## Description

GTC downstream intrrupt status

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:4|RESERVED||
|3|LOM|Super-Frame Loss of Synchronization.|
|2|DS_FEC_STS|Downstream FEC on/off status, detected from Ident field.|
|1|LOF|Status of Loss of Downstream Frame.|
|0|LOS|Loss of Signal. LOS = ((OPTIC_LOS_POLAR nxor OPTIC_LOS_SIG) and OPTIC_LOS_ENA) or ((CDR_LOS_POLAR nxor CDR_LOS_SIG) and CDR_LOS_ENA);|
