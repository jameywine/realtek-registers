---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: SC_P_CTRL_0

## Details

*Name* SC_P_CTRL_0

*Offset* 0x20014

*Feature* [CONGESTION_AVOIDANCE](../../feature/CONGESTION_AVOIDANCE)

*Bit Offset:* 32

*Port Range:* 0-10

## Description

Specify congestion timer control register.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:24|RESERVED||
|23:20|CGST_TMR_H|Half duplex Congest timer, unit in seconds|
|19:16|CGST_SUST_TMR_LMT_H|Half duplex Congest sustain timer limit, RW unit in seconds. If CNGST_TMR_H >= CNGST_SUST_TMR_LMT_H, this port will enter special congest state.<br>If CNGST_SUST_TMR_LMT_H!=0, this function is enabled.|
|15:8|RESERVED||
|7:4|CGST_TMR|Congest timer, unit in seconds.|
|3:0|CGST_SUST_TMR_LMT|Congest sustain timer limited, unit in seconds. If CGST_TMR>=CGST_SUST_TMR_LMT, this port will enter Special Congest State.<br>When CGST_SUST_TMR_LMT!=0, special congest function is enabled.|
