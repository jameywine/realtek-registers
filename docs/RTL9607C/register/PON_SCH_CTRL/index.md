---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: PON_SCH_CTRL

## Details

*Name* PON_SCH_CTRL

*Offset* 0xF021E0

*Feature* [PONIP_SCHEDULING_UPSTREAM](../../feature/PONIP_SCHEDULING_UPSTREAM)

## Description

PON Scheduling control register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:20|RESERVED||
|19|PON_WFQ_MODE|Scheduling type.<br>0b0: Weighted-Fair-Queue type<br>0b1: Weighted-Round-Robin type|
|18|PON_GEN_PIR_DROP|Set to 1 by SDK during ponmac init for unknown reason|
|17|METER_OP|0b0: Can’t consume token exceed requirement<br>0b1: consume token exceed requirement, and return to 0.|
|16|PON_WFQ_IFG|Rate calculation include IFG(Inter Frame Gap) setting in WFQ leaky bucket 0b0:exclude IPG 0b1:inculde IPG|
|15:0|PON_WFQ_BURSTSIZE|Bucket size (high threshold) of WFQ Leaky Bucket, unit bytes|
