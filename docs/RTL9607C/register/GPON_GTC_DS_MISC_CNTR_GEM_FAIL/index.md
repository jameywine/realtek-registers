---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GTC_DS_MISC_CNTR_GEM_FAIL

## Details

*Name* GPON_GTC_DS_MISC_CNTR_GEM_FAIL

*Offset* 0x7011C0

*Feature* [GTC_DOWNSTREAM](../../feature/GTC_DOWNSTREAM)

## Description

Dowmstream statistics.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|CNTR_PORTID_MMATCH|Counting the received GEM fragments which match multiple provisioned GEM port ID. This only happen when duplicated GEM port IDs are provisioned.|
|15:0|CNTR_GEM_LEN_MISM|Counter of GEM Packet length mismatch.|
