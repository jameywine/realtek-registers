---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: CFG_MAC_MISC

## Details

*Name* CFG_MAC_MISC

*Offset* 0x230FC

*Feature* [MAC_CONTROL](../../feature/MAC_CONTROL)

## Description

Miscellaneous MAC configurations

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:29|RESERVED||
|28|RESERVED||
|27|CFG_RX_USE_DSC_EN||
|26|CFG_TX_FIFO_RST||
|25|CFG_RX_FIFO_RST||
|24:15|RSVPG_BEFORE_FCDROP|Set reserve page (threshold) before triggering flow control drop|
|14|CHECK_MIN_IPG_RXDV||
|13:9|LIMIT_IPG_CFG||
|8|RX_IOL_MAX_LENGTH_CFG||
|7|RX_IOL_ERROR_LENGTH_CFG||
|6|RESERVED||
|5:0|RX_DV_CNT_CFG||
