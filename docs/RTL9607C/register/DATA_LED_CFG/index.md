---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: DATA_LED_CFG

## Details

*Name* DATA_LED_CFG

*Offset* 0x1E004

*Feature* [LED](../../feature/LED)

*Bit Offset:* 32

*Array Range:* 0-17

## Description

LED Source Register

Each LED supports several control sources. User can select one of the control sources by setting bits[20:16]. For these control sources, additional control bits[13:0] can be set for to choose different behaviour of those sources. Such as link speed, duplex and Tx/Rx activities. LED also support CPU force mode. When the bit[14] is set to 1, the force value can be controlled by register LED_FORCE_VALUE_CFG.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:21|RESERVED||
|20:16|LED_CFG|Select led port.<br>00000: Disable.<br>00001: UTP0<br>00010: UTP1<br>00011: UTP2<br>00100: UTP3<br>00101: UTP4<br>00110: Fiber<br>00111: HiSGMII0<br>01000: HiSGMII1<br>01001: RGMII<br>01010: CPU0<br>01011: CPU1<br>11011: PON<br>11100-11111: Reserved.<br>Note: USB/PCIE control by SW.|
|15|RESERVED||
|14|CPU_FORCE_MOD|cpu force LED|
|13|HSG_SPD2500|LED light when HSG link at Speed 2500|
|12|UTP_SPD1000|LED light when UTP link at Speed 1000|
|11|UTP_SPD500|LED light when UTP link at Speed 500|
|10|UTP_SPD100|LED light when UTP link at Speed 100|
|9|UTP_SPD10|LED light when UTP link at Speed 10|
|8|UTP_DUP|LED light when UTP link at full duplex mode|
|7|HSG_SPD2500_ACT|LED blink when HSG packet access at Speed 2500|
|6|UTP_SPD1000_ACT|LED blink when packet access at Speed 1000|
|5|UTP_SPD500_ACT|LED blink when packet access at Speed 500|
|4|UTP_SPD100_ACT|LED blink when packet access at Speed 100|
|3|UTP_SPD10_ACT|LED blink when packet access at Speed 10|
|2|UTP_RX_ACT|LED blink when RX packet access|
|1|UTP_TX_ACT|LED blink when TX packet access|
|0|UTP_COL|LED blink when collision occur|
