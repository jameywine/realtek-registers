---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: EPON_INTR

## Details

*Name* EPON_INTR

*Offset* 0x36020

*Feature* [EPON_CONFIGURATION](../../feature/EPON_CONFIGURATION)

## Description

EPON interrupt register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:25|RESERVED||
|24|EPON_ROUGE_ONT_TOO_LONG_IMS||
|23|EPON_ROUGE_ONT_TOO_LONG_IMR||
|22|EPON_ROUGE_ONT_MISMATCH_IMS||
|21|EPON_ROUGE_ONT_MISMATCH_IMR||
|20|EPON_1PPS_IMR||
|19|EPON_1PPS_IMS||
|18|RCOV_RXFEC_IMR||
|17|RCOV_RXFEC_IMS||
|16:9|MPCP_TIMEOUT_LLIDIDX|llid mpcp timeout mask|
|8|REG_RESULT||
|7|LOS_IMR|interrupt mask for LOS|
|6|REG_COMPLETE_IMR|IMR register LLID tx|
|5|TIME_DRIFT_IMR|IMR time drift|
|4|MPCP_TIMEOUT_IMR|IMR mpcp timeout|
|3|LOS_IMS|interrupt status for LOS.|
|2|REG_COMPLETE_IMS|interrupt staus for register LLID tx<br>write 1 clear|
|1|TIME_DRIFT_IMS|interrupt staus for time drift<br>write 1 clear|
|0|MPCP_TIMEOUT_IMS|interrupt staus for mpcp timeout<br>write 1 clear|
