---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GTC_US_OPTIC_SD_TH

## Details

*Name* GPON_GTC_US_OPTIC_SD_TH

*Offset* 0x705188

*Feature* [GTC_UPSTREAM](../../feature/GTC_UPSTREAM)

## Description

Optical SD threshold

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31|RESERVED||
|30:16|OPTIC_SD_MISM_THREH|The threshold of time for upstream optic SD signal mismatching with the output Burst Enable|
|15|RESERVED||
|14:0|OPTIC_SD_TOOLONG_THRESH|The threshold of time for upstream optic SD signal assertion time. In unit of upstream byte.|
