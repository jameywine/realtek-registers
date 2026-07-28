---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: PS_LINKID_GATCLK_CTRL

## Details

*Name* PS_LINKID_GATCLK_CTRL

*Offset* 0x23128

*Feature* [POWER_SAVING](../../feature/POWER_SAVING)

## Description

Specify link idle gating clock and link idle time control register.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:6|RESERVED||
|5:4|LINKID_TIME|When enable Link Idle Gating Clock Control Register and link idle time exceed LINKID_TIME, will trigger clock gating power saving mode.<br>0x0: 100 ms<br>0x1: 200 ms<br>0x2: 300 ms<br>0x3: 30 sec|
|3:0|RESERVED||
