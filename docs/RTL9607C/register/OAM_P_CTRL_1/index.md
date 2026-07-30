---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: OAM_P_CTRL_1

## Details

*Name* OAM_P_CTRL_1

*Offset* 0x170F0

*Feature* [OAM](../../feature/OAM)

*Bit Offset:* 1

*Port Range:* 0-10

## Description

OAM per-port control register 1

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|0|OAM_MULTIPLEXER|OAM MULTIPLEXER(transmitting multiplexing function) action.<br>0b00 FWD(default)<br>-Normal process<br>-Forwarding non-OAMPDUs<br>0b01-DISCARD<br>-Discarding non-OAMPDUs<br>0b10-CPUONLY<br>- Transmitting PDUs from CPU only.<br>0b11-reserved(as FWD)|
