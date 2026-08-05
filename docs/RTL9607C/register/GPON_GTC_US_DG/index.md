---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GTC_US_DG

## Details

*Name* GPON_GTC_US_DG

*Offset* 0x705184

*Feature* [GTC_UPSTREAM](../../feature/GTC_UPSTREAM)

## Description

ONU dying gasp

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:9|RESERVED||
|8|DG_STATUS|0x1: currently in Dying Gasp status|
|7:4|DG_MSG_TX_CNT|Counter of transmitted Dying Gasp messages|
|3:0|DG_MSG_TX_CNT_THRESHOLD|Threshold of counter of transmitted Dying Gasp message, once the count reaching this threshold, an interrupt may be generated.|
