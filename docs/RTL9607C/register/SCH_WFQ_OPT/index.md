---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: SCH_WFQ_OPT

## Details

*Name* SCH_WFQ_OPT

*Offset* 0x2D974

*Feature* [SCHEDULING](../../feature/SCHEDULING)

## Description

WFQ scheduling option register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:19|RESERVED||
|18|WFQ_TKN_CTRL|Token control? |
|17|WFQ_WTSCL||
|16|SCH_EN_WFQ_2ND_TH|Scheduling Enable WFQ 2nd threshold?|
|15:0|WFQ_BURSTSIZE_L|Bucket size (low threshold) of WFQ Leaky Bucket, unit bytes ? |
