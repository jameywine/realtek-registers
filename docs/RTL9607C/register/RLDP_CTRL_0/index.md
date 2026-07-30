---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: RLDP_CTRL_0

## Details

*Name* RLDP_CTRL_0

*Offset* 0x23228

*Feature* [RLDP](../../feature/RLDP)

## Description

RLDP protocol control 0

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:1|RESERVED||
|0|ACT_RUNOUTDSC|RLDP action while descriptors run-out state<br>1: Not drop RLDP packet besides DSC run out.<br>0: Drop RLDP packet when DSC run out.|
