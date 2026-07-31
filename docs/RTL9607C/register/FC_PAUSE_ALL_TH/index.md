---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: FC_PAUSE_ALL_TH

## Details

*Name* FC_PAUSE_ALL_TH

*Offset* 0x231A0

*Feature* [FLOWCONTROL_BACKPRESSURE_THRESHOLD](../../feature/FLOWCONTROL_BACKPRESSURE_THRESHOLD)

## Description

Specify flow control pause all threshold register.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:10|RESERVED||
|9:0|TH|Threshold of system page usage number is over this one and egress flow control is enabled, ASIC will force sending pause ON frame to all ports untill page usaging number is under this threshold, unit page|
