---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GEM_DS_FWD_CNTR_IND

## Details

*Name* GPON_GEM_DS_FWD_CNTR_IND

*Offset* 0x70404C

*Feature* [GEM_PORT_DOWNSTREAM](../../feature/GEM_PORT_DOWNSTREAM)

## Description

Downstream GEM port forward counter indictor

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15|ETH_PKT_FWD_R_ACK|Acknowledge of reading operation to CNTR_ETH_FWD.|
|14:7|RESERVED||
|6:0|ETH_PKT_FWD_IDX|GEM port index for CNTR_ETH_FWD.<br>ETH_PKT_FWD is 32-bit per GEM port counter.<br>The read procedure for it is<br>1. Write local GEM port index to ETH_PKT_FWD_IDX<br>2. Wait until ETH_PKT_FWD_R_ACK = ’1’<br>3. Read ETH_PKT_FWD|
