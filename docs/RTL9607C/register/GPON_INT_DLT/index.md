---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_INT_DLT

## Details

*Name* GPON_INT_DLT

*Offset* 0x700000

*Feature* [GPON_MAC_GENERAL_CONFIG](../../feature/GPON_MAC_GENERAL_CONFIG)

## Description

GPON MAC top interruption status

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15|GPON_IRQ|0x0: GPON MAC top interrupt output is inactive<br>0x1: GPON MAC top interrupt output is active GPON_IRQ = (GTC_DS_INTR and GTC_DS_M) or (GTC_DS_CAP_INTR and GTC_DS_CAP_M) or (AES_DECRYPT_INTR and AES_DECRYPT_M) or (GEM_DS_INTR and GEM_DS_M) or (GTC_US_INTR and GTC_US_M) or (GEM_US_INTR and GEM_US_M)|
|14:0|RESERVED||
