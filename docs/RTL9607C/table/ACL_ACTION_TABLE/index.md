---
tags:
  - RTL9607C
  - Table
  - Table Fields
---

# RTL9607C table: ACL_ACTION_TABLE

## Details

*Name* ACL_ACTION_TABLE

*Feature* [TABLE_ACCESS](../../feature/TABLE_ACCESS)

*Type* 3

*Entries* 128

*Control register* [TBL_ACCESS_CTRL](../../register/TBL_ACCESS_CTRL)

*Write Data register* [TBL_ACCESS_WR_DATA](../../register/TBL_ACCESS_WR_DATA)

*Read Data register* [TBL_ACCESS_RR_DATA](../../register/TBL_ACCESS_RR_DATA)

## Description

ACL action Table

## Fields

|Name|LSB|Bits|Description|
| :--- | :--- | :--- | :--- |
|HIT|63|1|ACL hit indicator (For Clasification Check)|
|ACLINT|62|1|ACL interrupt|
|PRIACT|59|3|Priority action<br>0x0: ACL Priority<br>0x1: DSCP Remarking<br>0x2: 1P Remarking<br>0x3: Policing<br>0x4: Logging|
|PRIDX|51|8|ACL priority/DSCP/1P Priority/Shared meter for Policing/Logging Counter MIB index|
|FWDACT|49|2|ACL forward decision<br>0x0: Copy frame with ACLPMSK<br>0x1: Redirect frame with ACLPMSK<br>0x2: Ingress mirror to ACLPMSK<br>0x3: Trap to CPU|
|FWD_PMSK|38|11|forwaring related port mask|
|POLICACT|36|2|0x0:Policing<br>0x1:Logging|
|METER_IDX|30|6|Share meter or Logging Counter MIB index|
|SACT|27|3|SVLAN action<br>0x0:Ingress SVLAN action(down stream only)<br>0x1:Egress SVLAN action(replace egress SVID only, both upstream and downstream)<br>0x2:Using CVID(SVID is C-tag, but S-member is from SVIDX_SACT, unstream only)<br>0x3:Policing<br>0x4:Logging<br>0x5:1p remark<br>0x6:dscp remark|
|SVID|15|12|SVID of SVLAN member configuration/Shared meter for Policing/Logging Counter MIB index/1P priority/dscp|
|CACT|12|3|CVLAN action type<br>0x0:Ingress CVLAN action<br>0x1:Egress CVLAN action(replace egress CVID only and CVID is inner 4K)<br>0x2:Using SVID(down stream only)<br>0x3:Policing<br>0x4:Logging<br>0x5:1p remark|
|CVID|0|12|CVID of CVLAN member configuration index/Shared meter for Policing/Logging Counter MIB index/1P priority|
