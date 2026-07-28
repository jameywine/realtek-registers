---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: WFQ_CTRL

## Details

*Name* WFQ_CTRL

*Offset* 0x2D800

*Feature* [SCHEDULING](../../feature/SCHEDULING)

## Description

Specify the WFQ related setting

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:18|RESERVED||
|17|WFQ_MODE|Scheduling type.<br>0b0: Weighted-Fair-Queue type<br>0b1: Weighted-Round-Robin type|
|16|WFQ_IFG|Rate calculation include IFG(Inter Frame Gap) setting in WFQ leaky bucket<br>0b0:exclude IPG<br>0b1:inculde IPG|
|15:0|WFQ_BURSTSIZE|Bucket size (high threshold) of WFQ Leaky Bucket, unit bytes|
