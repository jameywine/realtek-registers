---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GTC_US_TX_PATTERN_CTL

## Details

*Name* GPON_GTC_US_TX_PATTERN_CTL

*Offset* 0x705020

*Feature* [GTC_UPSTREAM](../../feature/GTC_UPSTREAM)

## Description

Tx pattern control. The register is protected.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:9|RESERVED||
|8|TX_PATTERN_MODE_NO_FG|0: FG mode denoted by TX_PATTERN_MODE_FG.<br>1: When TX_PATTERN_MODE_FG set to 3|
|7:6|RESERVED||
|5:4|TX_PATTERN_MODE_BG|0: Normal.<br>1: PRBS.<br>2: PRBS.<br>3: None.|
|3:2|RESERVED||
|1:0|TX_PATTERN_MODE_FG|0: Normal.<br>1: PRBS.<br>2: PRBS.<br>3: None. In that case TX_PATTERN_MODE_NO_FG is also set to 1.|
