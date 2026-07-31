---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: LED_BLINK_RATE_CFG

## Details

*Name* LED_BLINK_RATE_CFG

*Offset* 0x1E05C

*Feature* [LED](../../feature/LED)

## Description

LED Blinking Rate

The blinking rate of different LED control source can be configured seperately.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:6|RESERVED||
|5:3|SEL_LED_FORCE_RATE|select CPU force mode LED blink rate<br>000 = 32 ms<br>001 = 64 ms<br>010 = 128 ms<br>011 = 256 ms<br>100 = 512 ms<br>101 = 1024 ms<br>110 = 48 ms<br>111 = 96 ms|
|2:0|SEL_MAC_LED_RATE|select MAC LED blink rate<br>000 = 32 ms<br>001 = 64 ms<br>010 = 128 ms<br>011 = 256 ms<br>100 = 512 ms<br>101 = 1024 ms<br>110 = 48 ms<br>111 = 96 ms|
