---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: PRI_SEL_TBL_CTRL

## Details

*Name* PRI_SEL_TBL_CTRL

*Offset* 0x1C2D4

*Feature* [INGRESS_PRIORITY_DECISION](../../feature/INGRESS_PRIORITY_DECISION)

*Bit Offset:* 32

*Array Range:* 0-3

## Description

Configure priority decision weight values register.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:15|RESERVED||
|14:12|SVLAN_WEIGHT|Internal priority decision weight configuration of SVLAN based priority source|
|11:9|ACL_WEIGHT|Internal priority decision weight configuration of ACL priority source|
|8:6|DSCP_WEIGHT|Internal priority decision weight configuration of DSCP based priority source|
|5:3|DOT1Q_WEIGHT|Internal priority decision weight configuration of 802.1Q based priority source|
|2:0|PORT_WEIGHT|Internal priority decision weight configuration of port based priority source|
