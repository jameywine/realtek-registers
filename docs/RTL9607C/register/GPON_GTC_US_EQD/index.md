---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GTC_US_EQD

## Details

*Name* GPON_GTC_US_EQD

*Offset* 0x705044

*Feature* [GTC_UPSTREAM](../../feature/GTC_UPSTREAM)

## Description

EqD configuration

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:27|RESERVED||
|26:24|EQD1_MULTFRAME|EqD configuration parameter of multi-frame.|
|23:18|RESERVED||
|17:0|EQD1_INFRAME|EqD configuration parameter of intra-frame.<br>Provided Software get EQD from OLT through Ranging_Time message, then<br>EQD1 = PLOAM_EQD + MIN_DELAY1 * 16 * 8;<br>EQD1_MULTIFRAME = EQD1/ (19440 * 8);<br>EQD1_INFRAME = EQD1_MULTIFRAME * 19440 * 8;|
