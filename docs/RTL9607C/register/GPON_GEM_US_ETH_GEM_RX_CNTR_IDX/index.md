---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GEM_US_ETH_GEM_RX_CNTR_IDX

## Details

*Name* GPON_GEM_US_ETH_GEM_RX_CNTR_IDX

*Offset* 0x706048

*Feature* [GEM_UPSTREAM](../../feature/GEM_UPSTREAM)

## Description

GEM upstream received ether or gem counter index

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15|ETH_GEM_RX_R_ACK|Acknowledge of reading operation to ETH_GEM_RX_CNTR.|
|14:8|RESERVED||
|7:0|ETH_GEM_RX_IDX|GEM port index for CNTR_ETH_RX. Or GEM RX.<br>Highest bit for ETH (1) or GEM(0).<br>Others, for GEM Port index.|
