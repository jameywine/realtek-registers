---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: SDS_REG12

## Details

*Name* SDS_REG12

*Offset* 0x40830

*Feature* [PHY_SERDES](../../feature/PHY_SERDES)

## Description

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15:8|SP_CFG_INB_TIMEOUT||
|7:4|SP_ABILITY|serdes ability = {5G, 2.5G, 1.25G}<br>ability{0} = 1’b0: auto mode<br>ability{0} = 1’b1: force mode, the force value is ability{3:1}|
|3|SP_CFG_AFE_40B||
|2|SP_SD_DET_ALGOR||
|1|SP_AUTO_DET_ALGOR||
|0|SP_SEND_NP_ON|send next page on, the next page of serdes N-way<br>0: serdes N-way will only send base page register<br>1: serdes N-way will send next page register after base page register|
