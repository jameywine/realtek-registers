---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: OAM_P_EN

## Details

*Name* OAM_P_EN

*Offset* 0x170F4

*Feature* [OAM](../../feature/OAM)

*Bit Offset:* 1

*Port Range:* 0-10

## Description

OAM per-port enable register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|0|EN|forwarding action of trapped oam PDU on specified port<br>0b0: disable (i.e forward)<br>0b1: enable OAM function and will trap OAM packet to CPU|
