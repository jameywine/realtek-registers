---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: PROBE_SELECT_US

## Details

*Name* PROBE_SELECT_US

*Offset* 0xF05400

*Feature* [CPU_IF](../../feature/CPU_IF)

## Description

PON Upstream Probe Select register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:8|RESERVED||
|7:5|R_DBG_FUNC_SEL|SDK sets bit 6 during PBO init. Maybe similar to what PROB_SEL does in NIC_PROBE_SELECT register?|
|4|RESERVED||
|3:0|DBG_SEL||
