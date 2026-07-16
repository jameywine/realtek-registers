---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: CHANGE_DUPLEX_CTRL

## Details

*Name* CHANGE_DUPLEX_CTRL

*Offset* 0x23120

*Feature* [MAC_CONTROL](../../feature/MAC_CONTROL)

## Description

Change Duplex Control register.

Note from SDK:
This function only apply to local N-way enable but link
partner in force mode. In that way, the local link status
will be 100Mb/half duplex. This function will change
local link status to 100Mb/full duplex under specific
condition.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:8|RESERVED||
|7|CFG_CHG_DUP_EN|1: Enable change duplex function|
|6:2|CFG_CHG_DUP_THR||
|1|CFG_CHG_DUP_CONGEST||
|0|RESERVED||
