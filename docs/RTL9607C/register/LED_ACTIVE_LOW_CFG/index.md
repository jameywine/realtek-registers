---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: LED_ACTIVE_LOW_CFG

## Details

*Name* LED_ACTIVE_LOW_CFG

*Offset* 0x1E04C

*Feature* [LED](../../feature/LED)

*Bit Offset:* 1

*Array Range:* 0-17

## Description

Parallel LED active high/low Register

For parallel LED mode the active mode is controlled by this register. The polarity of each parallel LED can be configured seperately.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|0|LED_POLARITY_INV|Invert LED polarity.<br>0: Normal<br>1: Invert|
