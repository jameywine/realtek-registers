---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GTC_DS_CFG

## Details

*Name* GPON_GTC_DS_CFG

*Offset* 0x701014

*Feature* [GTC_DOWNSTREAM](../../feature/GTC_DOWNSTREAM)

## Description

GTC downstream configuration

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:12|RESERVED||
|11|BWM_NO_FLT||
|10|BWM_FILT_ONUID|0x0: Accept all BWMap items, for debug.<br>0x1: Only accept BWMap items matching provisioned T-CONTs.|
|9|CHK_BWM_CRC|0x0: Accept BWMap items even with CRC error, for debug.<br>0x1: Only accept BWMap items which has not CRC error.|
|8|PLEND_STRICT_MODE|0x0: processing in standard mode.<br>0x1: process received PLENd in strict mode, only 2 usable matching PLENd structures are accepted.|
|7:6|EXTRA_SN_TX|Times of Extra SN transmission, defined in Upstream Overhead PLOAMd message.<br>This function is deprecated in latest G.984.3.|
|5|DIS_NORMALIZE||
|4|FEC_CORRECT_DIS|0x0: Enable downstream FEC correction.<br>0x1: Disable downstream FEC correction even when DS FEC encoding is enabled. The encoded parity bytes are ignored and the data will be passed to following processing modules.|
|3:1|FEC_DET_THRSH|Downstream FEC status detection threshold, number of GPON frames.<br>By default, it should be set to 1. Only keep this configurable just to improve compatibility.|
|0|DESCRAM_DIS|0x0: Enable de-scrambling.<br>0x1: Disable de-scrambling.<br>Only for debugging.|
