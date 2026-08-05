---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GTC_US_WRITE_PROTECT

## Details

*Name* GPON_GTC_US_WRITE_PROTECT

*Offset* 0x705018

*Feature* [GTC_UPSTREAM](../../feature/GTC_UPSTREAM)

## Description

Write protection

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15:0|RSV_REG_WRITE_PROTECTION|Write protection register for reserved registers. What’s protected includes registers of GTC_US_CFG, GTC_US_MIN_DELAY, and GTC_US_PROC_MODE.<br>Only when the write protection register is equal to 0xCC19 these protected registers can be changed.|
