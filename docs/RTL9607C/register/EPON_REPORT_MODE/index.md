---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: EPON_REPORT_MODE

## Details

*Name* EPON_REPORT_MODE

*Offset* 0xF029E4

*Feature* [PONIP_SCHEDULING_UPSTREAM](../../feature/PONIP_SCHEDULING_UPSTREAM)

## Description

EPON Report mode register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|REPORT_CNT_ADJ|adjust report value in TQ.|
|15:3|RESERVED||
|2:0|REPORT_MODE|Report mode.<br>0: Normal.<br>2: Force 0.<br>3: Force F.<br>4: 0 F|
