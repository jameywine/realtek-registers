---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: EPON_FEC_CONFIG

## Details

*Name* EPON_FEC_CONFIG

*Offset* 0x36000

*Feature* [EPON_CONFIGURATION](../../feature/EPON_CONFIGURATION)

## Description

FEC configuration register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:22|RESERVED||
|21:16|FEC_OVER_TX|FEC Overhead|
|15|BYPASS_FEC|1’b1: bypass FEC operation and reduce pkt latency|
|14|DVSE_TPAR||
|13:11|DVS_TPAR||
|10|DVSE_DAT||
|9:7|DVS_DAT||
|6|DVSE_RPAR||
|5:3|DVS_RPAR||
|2|RESERVED||
|1|FEC_US_EN|enable down stream FEC|
|0|FEC_DS_EN|enable up stream FEC|
