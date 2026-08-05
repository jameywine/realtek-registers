---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: FT_TRF

## Details

*Name* FT_TRF

*Offset* 0x800000

*Feature* [FLOW_TRAFFIC_TABLE](../../feature/FLOW_TRAFFIC_TABLE)

*Bit Offset:* 32

*Array Range:* 0-1023

## Description

Flow Traffic Table register.

Used in rtk_rg_asic_flowTrfIndicator_get(), rtk_rg_asic_flowTraffic_get(), rtk_rg_asic_flowValidBit_get() functions.

Array range is for position of flow entry index?

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:0|TRF|flow traffic bits|
