---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: SDS_REG0

## Details

*Name* SDS_REG0

*Offset* 0x40800

*Feature* [PHY_SERDES](../../feature/PHY_SERDES)

## Description

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15|SP_DIS_RENWAY||
|14|SP_BYP_8B10B|bypass the 8b10b encode/decode<br>0: normal<br>1: bypass the 8b10b encode/decode|
|13:12|SP_CDET|dynamic comma detect function enable when alignment is done<br>cdet[0] = 1’b0: auto mode<br>cdet[0] = 1’b1: force mode, the force value is cdet[1]|
|11|SP_DIS_TMR_CMA|disable comma timeout monitor function<br>0: enable comma timeout monitor<br>1: disable comma timeout monitor|
|10|SP_DIS_APX||
|9|SP_INV_HSI|invert the serdes input 20-bit data (polarity change manually)<br>0: normal<br>1: invert the input 20-bit data|
|8|SP_INV_HSO|invert the serdes output 20-bit data (polarity change manually)<br>0: normal<br>1: invert the output 20-bit data|
|7:6|SP_SDS_SDET_DEG|sds_sdet input deglitch or not<br>00: disable the deglitch function<br>01: tolerant 4 cycle glitch<br>10: tolerant 8 cycle glitch<br>11: tolerant 16 cycle glitch|
|5|SP_CFG_AFE_FEC_LPK||
|4|SP_CFG_DIG_LPK||
|3|SP_CFG_REM_LPK|analog remote loopback, loopback just come into the digital circuit|
|2|SP_SDS_TX_DOWN|serdes TX down, the d2analog 20-bit data will be zero|
|1|SP_SDS_EN_RX|serdes enable RX|
|0|SP_SDS_EN_TX|serdes enable TX|
