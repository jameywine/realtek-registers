---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: RX_CFG_US

## Details

*Name* RX_CFG_US

*Offset* 0xF04044

*Feature* [PONNIC_CTRL](../../feature/PONNIC_CTRL)

## Description

PONNIC Upstream RX Configuration Register
SDK only sets AER bit during PBO init.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:10|RESERVED||
|9:8|R_PREAMBLE_LEN||
|7|RESERVED||
|6|AFLOW|Accept flow control : When set to 1, flow control packet will also be received & DMA to rx buffer for debug. Default is 0|
|5|AER|Accept Error Packet: When set to 1, all packets with CRC error, alignment error, and/or collided fragments will be accepted. When set to 0, all packets with CRC error, alignment error, and/or collided fragments will be rejected|
|4|AR|Accept Runt: This bit allows the receiver to accept packets that are smaller than 64 bytes. The packet must be at least 8 bytes long to be accepted as a runt. Set to 1 to accept runt packets|
|3|AB|Set to 1 to accept broadcast packets, 0 to reject.|
|2|AM|Set to 1 to accept multicast packets, 0 to reject.|
|1|APM|Set to 1 to accept physical match packets, 0 to reject.|
|0|AAP|Set to 1 to accept all packets with physical destination address, 0 to reject|
