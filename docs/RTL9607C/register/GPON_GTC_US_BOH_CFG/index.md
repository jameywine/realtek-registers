---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GTC_US_BOH_CFG

## Details

*Name* GPON_GTC_US_BOH_CFG

*Offset* 0x705054

*Feature* [GTC_UPSTREAM](../../feature/GTC_UPSTREAM)

## Description

Upsteam Burst Overhead configuration

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:12|RESERVED||
|11:8|BOH_REPEAT|Nth byte of BOH_DATA will be repeated to get total overhead to reach length BOH_LENGTH. Here N is BOH_REPEAT.<br>Valid value: 0x1-0xB.|
|7:0|BOH_LENGTH|Length of Upstream Burst Overhead (Preamble and Delimiter, including Guard Bits).|
