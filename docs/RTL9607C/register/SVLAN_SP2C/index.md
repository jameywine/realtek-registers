---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: SVLAN_SP2C

## Details

*Name* SVLAN_SP2C

*Offset* 0x2A034

*Feature* [_IEEE802_1AD_PROVIDER_BRIDGES_Q_IN_Q](../../feature/_IEEE802_1AD_PROVIDER_BRIDGES_Q_IN_Q)

*Bit Offset:* 32

*Array Range:* 0-63

## Description

Downstream SVLAN + Egress port to CVID configuration

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:29|PRIORITY||
|28:17|EGRVID|Egressing CVID|
|16:13|DST_PORT|Egressing customer port number of s-tag packet from uplink ports in SP2C configuration|
|12:1|IGRVID|Ingress CVID|
|0|VALID|Valid setting|
