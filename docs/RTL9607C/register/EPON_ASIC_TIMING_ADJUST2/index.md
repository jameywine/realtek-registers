---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: EPON_ASIC_TIMING_ADJUST2

## Details

*Name* EPON_ASIC_TIMING_ADJUST2

*Offset* 0x36008

*Feature* [EPON_CONFIGURATION](../../feature/EPON_CONFIGURATION)

## Description

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:27|RESERVED||
|26:25|DY_ADJ_BC||
|24:20|LSR_OFF_SHIFT|laser off shift, for debug purpose|
|19:15|LSR_ON_SHIFT|laser on shift, for debug purpose|
|14:0|ADJ_BC|adjust data byte count of each grant<br>15’d0 : default (data byte conut = grant length )<br>15’d1 : default (data byte conut = grant length - 1)<br>15’d2 : default (data byte conut = grant length - 2)<br>15’d3 : default (data byte conut = grant length - 3)<br>...|
