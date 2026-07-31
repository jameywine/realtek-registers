---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: FC_DROP_ALL_TH

## Details

*Name* FC_DROP_ALL_TH

*Offset* 0x2319C

*Feature* [FLOWCONTROL_BACKPRESSURE_THRESHOLD](../../feature/FLOWCONTROL_BACKPRESSURE_THRESHOLD)

## Description

Specify flow control drop all threshold register.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:10|RESERVED||
|9:0|TH|Flow control force drop(run-out) threshold. ASIC will force drop incoming packet while total page used counter is over this setting unit page|
