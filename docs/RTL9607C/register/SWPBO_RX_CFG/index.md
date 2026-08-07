---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: SWPBO_RX_CFG

## Details

*Name* SWPBO_RX_CFG

*Offset* 0xF14044

*Feature* [SWPBO_NIC_CTRL](../../feature/SWPBO_NIC_CTRL)

## Description

Switch PBO PON NIC RX configuration

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:10|RESERVED||
|9:8|R_PREAMBLE_LEN|Set to 0x1 by SDK during PBO init|
|7|RESERVED||
|6|AFLOW||
|5|AER|Accept Error Packet: When set to 1, all packets with CRC error, alignment error, and/or collided fragments will be accepted. When set to 0, all packets with CRC error, alignment error, and/or collided fragments will be rejected|
|4|AR||
|3|AB||
|2|AM||
|1|APM||
|0|AAP||
