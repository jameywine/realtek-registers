---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GEM_DS_RX_CNTR_IND

## Details

*Name* GPON_GEM_DS_RX_CNTR_IND

*Offset* 0x704040

*Feature* [GEM_PORT_DOWNSTREAM](../../feature/GEM_PORT_DOWNSTREAM)

## Description

Downstream GEM port rx counter indictor

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15|ETH_PKT_RX_R_ACK|Acknowledge of reading operation to CNTR_ETH_RX.|
|14:7|RESERVED||
|6:0|ETH_PKT_RX_IDX|GEM port index for CNTR_ETH_RX.<br>ETH_PKT_RX is 32-bit per GEM port counter.<br>The read procedure for it is<br>1. Write local GEM port index to ETH_PKT_RX_IDX<br>2. Wait until ETH_PKT_RX_R_ACK = ’1’<br>3. Read ETH_PKT_RX|
