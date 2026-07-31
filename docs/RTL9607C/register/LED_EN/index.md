---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: LED_EN

## Details

*Name* LED_EN

*Offset* 0x1E068

*Feature* [LED](../../feature/LED)

## Description

LED enable Register.

The LED IO PIN must be enabled first, and then its PIN can start working as LED mode.

For parallel LED, each LED IO PIN must be enabled individually. The both IO and LED must be enabled.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:26|RESERVED||
|25|LED_SERI_DATA_EN|Enable serial LED data<br>0b0: Disable<br>0b1: Enable|
|24:19|RESERVED||
|18|LED17_PARA_EN|Enable parallel LED17.<br>0b0: Disable<br>0b1: Enable|
|17|LED16_PARA_EN|Enable parallel LED16.<br>0b0: Disable<br>0b1: Enable|
|16|LED15_PARA_EN|Enable parallel LED15.<br>0b0: Disable<br>0b1: Enable|
|15|LED14_PARA_EN|Enable parallel LED14.<br>0b0: Disable<br>0b1: Enable|
|14|LED13_PARA_EN|Enable parallel LED13.<br>0b0: Disable<br>0b1: Enable|
|13|LED12_PARA_EN|Enable parallel LED12.<br>0b0: Disable<br>0b1: Enable|
|12|LED11_PARA_EN|Enable parallel LED11.<br>0b0: Disable<br>0b1: Enable|
|11|LED10_PARA_EN|Enable parallel LED10.<br>0b0: Disable<br>0b1: Enable|
|10|LED9_PARA_EN|Enable parallel LED9.<br>0b0: Disable<br>0b1: Enable|
|9|LED8_PARA_EN|Enable parallel LED8.<br>0b0: Disable<br>0b1: Enable|
|8|LED7_PARA_EN|Enable parallel LED7.<br>0b0: Disable<br>0b1: Enable|
|7|LED6_PARA_EN|Enable parallel LED6.<br>0b0: Disable<br>0b1: Enable|
|6|LED5_PARA_EN|Enable parallel LED5.<br>0b0: Disable<br>0b1: Enable|
|5|LED4_PARA_EN|Enable parallel LED4.<br>0b0: Disable<br>0b1: Enable|
|4|LED3_PARA_EN|Enable parallel LED3.<br>0b0: Disable<br>0b1: Enable|
|3|LED2_PARA_EN|Enable parallel LED2.<br>0b0: Disable<br>0b1: Enable|
|2|LED1_PARA_EN|Enable parallel LED1.<br>0b0: Disable<br>0b1: Enable|
|1|LED0_PARA_EN|Enable parallel LED0.<br>0b0: Disable<br>0b1: Enable|
|0|RESERVED||
