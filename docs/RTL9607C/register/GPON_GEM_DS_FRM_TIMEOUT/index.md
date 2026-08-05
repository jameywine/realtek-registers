---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GEM_DS_FRM_TIMEOUT

## Details

*Name* GPON_GEM_DS_FRM_TIMEOUT

*Offset* 0x704098

*Feature* [GEM_PORT_DOWNSTREAM](../../feature/GEM_PORT_DOWNSTREAM)

## Description

Downstream GEM block multicast read data

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15:14|DEBUG_BUS_SEL||
|13:9|RESERVED||
|8|OMCI_TR_MODE|0x0: OMCI Forward without bank treatment.<br>0x1: OMCI Forward with bank treatment.|
|7:5|RESERVED||
|4:0|ASSM_TIMEOUT_FRM|Number of GPON Frames for assembly timeout threshold.|
