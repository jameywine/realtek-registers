---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: DYNGASP_CTRL

## Details

*Name* DYNGASP_CTRL

*Offset* 0x29C

*Feature* [CHP_INFORMATION](../../feature/CHP_INFORMATION)

## Description

Dying Gasp Control Register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|GASP_DGC_TIMER||
|15|GASP_FORCE||
|14:8|RESERVED||
|7|DYNGASP_OUT_2_INV||
|6|DYNGASP_OUT_2_EN||
|5|DYNGASP_OUT_1_INV||
|4|DYNGASP_OUT_1_EN||
|3|DYNGASP_CMP_INV|dyinggasp comparison result polarity inversion|
|2|DYNGASP_OUT_INV|dyinggasp output pin polarity inversion|
|1|DYNGASP_OUT_EN|dyinggasp output pin driving enable|
|0|DYNGASP_OUT_PULL|dyinggasp output pin pull polarity|
