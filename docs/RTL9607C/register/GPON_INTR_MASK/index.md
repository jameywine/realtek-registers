---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_INTR_MASK

## Details

*Name* GPON_INTR_MASK

*Offset* 0x700040

*Feature* [GPON_MAC_GENERAL_CONFIG](../../feature/GPON_MAC_GENERAL_CONFIG)

## Description

GPON MAC TOP interrupt mask

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:7|RESERVED||
|6|GEM_US_M|0x0: prevent GEM_US_INTR from contributing to generation of GPON MAC TOP interrupt.<br>0x1: GEM_US_INTR can generate interrupt.|
|5|GTC_US_M|0x0: prevent "GTC_US_INTR" from contributing to generation of GPON MAC TOP interrupt.<br>0x1: GTC_US_INTR can generate interrupt.|
|4|GEM_DS_M|0x0: prevent "GEM_DS_INTR" from contributing to generation of GPON MAC TOP interrupt.<br>0x1: GEM_DS_INTR can generate interrupt.|
|3|AES_DECRYPT_M|0x0: prevent "AES_DECRYPT_INTR" from contributing to generation of GPON MAC TOP interrupt.<br>0x1: AES_DECRYPT_INTR can generate interrupt.|
|2|GTC_DS_CAP_M|0x0: prevent "GTC_DS_CAP_INTR" from contributing to generation of GPON MAC TOP interrupt.<br>0x1: GTC_DS_CAP__INTR can generate interrupt.|
|1|GTC_DS_M|0x0: prevent "GTC_DS_INTR" from contributing to generation of GPON MAC TOP interrupt.<br>0x1: GTC_DS_INTR can generate interrupt.|
|0|DUMMY_M||
