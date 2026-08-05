---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GTC_US_PROC_MODE

## Details

*Name* GPON_GTC_US_PROC_MODE

*Offset* 0x705200

*Feature* [GTC_UPSTREAM](../../feature/GTC_UPSTREAM)

## Description

Processing mode. The register is protected.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:2|RESERVED||
|1|OPTIC_AUTO_SUPRESS_DIS|0x1: Disable the function of suppressing laser when ONT is outside of state 3, 4 and 5.<br>Should not be changed, only for debug.|
|0|AUTO_PROC_SSTART|0x1: Process Small SSTART (< BOH LEN) automatically.<br>Should not be changed, only for debug.|
