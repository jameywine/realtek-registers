---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: SWITCH_CTRL

## Details

*Name* SWITCH_CTRL

*Offset* 0x23110

*Feature* [MAC_CONTROL](../../feature/MAC_CONTROL)

## Description

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:10|RESERVED||
|9|KEEP_CGST_PAT_ORG||
|8|BKPR_DEF_PAT||
|7:6|BKPR_IPG||
|5|LDNDRN_ORG||
|4|PKTDRN_ORG||
|3:2|CRCRECAL||
|1|SHORT_IPG|cfg_ifgsel can be used|
|0|PAUSE_MAX128|0:Maximum of 128 consecutive pause frames<br>1:Infinite pause frame count|
