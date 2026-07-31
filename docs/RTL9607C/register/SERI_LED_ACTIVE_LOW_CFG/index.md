---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: SERI_LED_ACTIVE_LOW_CFG

## Details

*Name* SERI_LED_ACTIVE_LOW_CFG

*Offset* 0x1E050

*Feature* [LED](../../feature/LED)

## Description

Serial LED active high/low Register

For serial LED mode the active mode is controlled by this register. it is a global configuration for all LEDs.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:1|RESERVED||
|0|SERI_LED_POLARITY_INV|Invert LED polarity.<br>0: Normal<br>1: Invert|
