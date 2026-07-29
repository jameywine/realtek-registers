---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: ACL_ACTION

## Details

*Name* ACL_ACTION

*Offset* 0x15050

*Feature* [INGRESS_ACL](../../feature/INGRESS_ACL)

*Bit Offset:* 32

*Array Range:* 0-127

## Description

ACL action configuration

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:7|RESERVED||
|6|NOT|NOT operation of ACL|
|5|INT_CF|Interrupt and classifcation control|
|4|FWD|Forwading action control|
|3|POLICING|Policing action control|
|2|PRI|Priority action control|
|1|SVLAN|SVLAN action control|
|0|CVLAN|CVLAN action control|
