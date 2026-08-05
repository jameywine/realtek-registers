---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GTC_DS_ETH_PTI

## Details

*Name* GPON_GTC_DS_ETH_PTI

*Offset* 0x701208

*Feature* [GTC_DOWNSTREAM](../../feature/GTC_DOWNSTREAM)

## Description

User data payload type indicator

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:7|RESERVED||
|6:4|ETH_PTI_MASK|PTI mask for user data.|
|3|RESERVED||
|2:0|ETH_END_PTI|PTI pattern of user data end fragment<br>For non-OMCI GEM, the end fragment is identified by: (received_PTI AND ETH_PTI_MASK) == ETH_END_PTI|
