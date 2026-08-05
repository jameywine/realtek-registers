---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GTC_DS_OMCI_PTI

## Details

*Name* GPON_GTC_DS_OMCI_PTI

*Offset* 0x701204

*Feature* [GTC_DOWNSTREAM](../../feature/GTC_DOWNSTREAM)

## Description

OMCI payload type indicator

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:7|RESERVED||
|6:4|OMCI_PTI_MASK|PTI mask for OMCI|
|3|RESERVED||
|2:0|OMCI_END_PTI|PTI pattern of OMCI end fragment<br>For OMCI GEM, the end fragment is identified by: (received_PTI AND OMCI_PTI_MASK) == OMCI_END_PTI|
