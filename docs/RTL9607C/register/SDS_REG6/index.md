---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: SDS_REG6

## Details

*Name* SDS_REG6

*Offset* 0x40818

*Feature* [PHY_SERDES](../../feature/PHY_SERDES)

## Description

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15|SP_CFG_NO_GIGA_SCM||
|14|SP_CFG_RE_SYNC_STYLE||
|13|SP_CFG_SYNC_GAT||
|12|SP_CFG_BYPSCR_XSG||
|11:8|SP_RX_BYPSCR|Scrambler RX bypass, 4-bit for {ch3, ch2, ch1, ch0}<br>0: RX enable scrambler<br>1: RX disable scrambler|
|7:4|SP_CFG_SLP_RQ||
|3:0|SP_TX_BYPSCR|Scrambler TX bypass, 4-bit for {ch3, ch2, ch1, ch0}<br>0: TX enable scrambler<br>1: TX disable scrambler|
