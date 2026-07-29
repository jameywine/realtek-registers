---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: RNG_CHK_VID_RNG

## Details

*Name* RNG_CHK_VID_RNG

*Offset* 0x15254

*Feature* [RANGE_CHECK_PORT_VLAN_IP_L4PORT_](../../feature/RANGE_CHECK_PORT_VLAN_IP_L4PORT_)

*Bit Offset:* 32

*Array Range:* 0-15

## Description

VID range check configuration

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:26|RESERVED||
|25:24|TYPE|Range checking data type<br>0x0:non-valid<br>0x1:CVLAN VID range check<br>0x2:SVLAN VID range check<br>0x3:reserved|
|23:12|VID_UPPER|VID range upper bound|
|11:0|VID_LOWER|VID range lower bound|
