---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: REGCTRL_GLB

## Details

*Name* REGCTRL_GLB

*Offset* 0x2300C

*Feature* [INTERFACE](../../feature/INTERFACE)

## Description

GPHY’s ocp timeout (unit:8ns)

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:27|RESERVED||
|26:22|PHY_OCP_TO_FLAG|flag indicate that gphy access failed by OCP (per GPHY)|
|21:17|PHY_OCP_TO|Timeout setting for GPHY access via OCP (unit:16ns), default is 4096ns|
|16:1|PHY_ACK_TO|Timeout setting for GPHY access via SMI (unit: 8192ns), default is 537us|
|0|RESERVED||
