---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: EPON_DEBUG1

## Details

*Name* EPON_DEBUG1

*Offset* 0x36014

*Feature* [EPON_CONFIGURATION](../../feature/EPON_CONFIGURATION)

## Description

EPON debug register 1

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:17|RESERVED||
|16|MODE0_7FFF_HANDLE|Set to 1 by SDK for "TK OLT issue"|
|15|CHURN_MODE|Churning Key Mode<br>0: Normal.<br>BL|
|14|IGNORE_MPCP_CRC||
|13|DIS_RANDOM_DELAY_EN|enable random delay|
|12|MODE0_INVALID_HDL|Mode 0 but LLID not match local LLID table handle<br>0: drop<br>1: trap to CPU|
|11|MODE1_INVALID_HDL|Mode 1 but LLID not match local LLID table handle<br>0: drop<br>1: trap to CPU|
|10|RESERVED||
|9:0|DBG_SEL|selection for debug signals|
