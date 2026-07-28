---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: EEE_EEEP_PORT_CTRL

## Details

*Name* EEE_EEEP_PORT_CTRL

*Offset* 0x2000C

*Feature* [POWER_SAVING](../../feature/POWER_SAVING)

*Bit Offset:* 32

*Port Range:* 0-10

## Description

EEEP per port control.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:12|RESERVED||
|11|EEE_TX_STS|Indicate the per port EEE or EEEP TX LPI status (read to clear)<br>0b0: the port TX is in normal state.<br>0b1: the port TX is in LPI state.|
|10|EEE_RX_STS|Indicate the per port EEE or EEEP RX LPI status (read to clear)<br>0b0: the port RX is in normal state.<br>0b1: the port RX is in LPI state.|
|9:2|RESERVED||
|1|EEE_PORT_TX_EN|Enable MAC EEE Tx function|
|0|EEE_PORT_RX_EN|Enable MAC EEE Rx function|
