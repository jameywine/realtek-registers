---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_INTR_STS

## Details

*Name* GPON_INTR_STS

*Offset* 0x700044

*Feature* [GPON_MAC_GENERAL_CONFIG](../../feature/GPON_MAC_GENERAL_CONFIG)

## Description

GPON MAC TOP interrupt status

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:7|RESERVED||
|6|GEM_US_INTR|Interrupt status of GEM_US, this bit keeps RO the same value with GEM_US_INTR in FILE GemUS.|
|5|GTC_US_INTR|Interrupt status of GTC_US, this bit keeps the same value with GTC_US_INTR in FILE GtcUs.|
|4|GEM_DS_INTR|Interrupt status of GEM_DS, this bit keeps the same value with GEM_DS_INTR in FILE GemDs.|
|3|AES_DECRYPT_INTR|Interrupt status of AES_DECRYPT, this bit keeps the same value with AES_DECRYPT_INTR in FILE AesDecrypt.|
|2|GTC_DS_CAP_INTR|Interrupt status of GTC_DS_CAP, this bit keeps the same value with GTC_DS_CAP_INTR in FILE xxx.|
|1|GTC_DS_INTR|Interrupt status of GTC_DS, this bit keeps the same value with GTC_DS_INTR in FILE GtcDs.|
|0|RESERVED||
