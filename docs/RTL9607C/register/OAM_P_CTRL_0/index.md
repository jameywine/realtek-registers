---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: OAM_P_CTRL_0

## Details

*Name* OAM_P_CTRL_0

*Offset* 0x170EC

*Feature* [OAM](../../feature/OAM)

*Bit Offset:* 2

*Port Range:* 0-10

## Description

OAM per-port control register 0

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|1:0|OAM_PARSER|OAM layer PARSER(receiving parsing function) action.<br>0b00-FWD(default)<br>-Normal process<br>-Forwarding non-OAMPDUs<br>0b01-LB(loopback)<br>-Looping back non-OAMPDUs,<br>-drop CRC and receiving FAILED packets<br>-trap OAMPDUs to CPU<br>0b10-DISCARD|
