---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: EPON_DEBUG2

## Details

*Name* EPON_DEBUG2

*Offset* 0x36018

*Feature* [EPON_CONFIGURATION](../../feature/EPON_CONFIGURATION)

## Description

EPON debug register 2

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:29|RESERVED||
|28:24|PRB_GN|select which grant to probe out on debug signals<br>5’d0: grant0 on debug signals<br>5’d1: grant1 on debug signals<br>5’d3: grant2 on debug signals|
|23:0|PRB_EPMC|debug signals for register to read|
