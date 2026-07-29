---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: CF_CFG

## Details

*Name* CF_CFG

*Offset* 0x16004

*Feature* [FLOW_CLASSIFICATION_FLOW_TABLE_](../../feature/FLOW_CLASSIFICATION_FLOW_TABLE_)

## Description

Classification function configuration

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:4|RESERVED||
|3:1|CF_TRAP_PRI|CF trap priority|
|0|CF_US_PERMIT|Permit packet which unmatch upstream classification rules<br>0b0: permit as normal forward<br>0b1: permit without PON port forwarding|
