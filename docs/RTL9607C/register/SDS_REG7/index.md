---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: SDS_REG7

## Details

*Name* SDS_REG7

*Offset* 0x4081C

*Feature* [PHY_SERDES](../../feature/PHY_SERDES)

## Description

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15|SP_CFG_8B10B_NO_CREXT||
|14|SP_CFG_NEG_CLKWR_A2D||
|13|SP_CFG_MIIXF_TS1K||
|12|SP_CFG_DLY_PRE8||
|11|SP_CFG_GRXD_SEL||
|10|SP_CFG_LPI_CMD_MII|lpi command surpport mii interface|
|9|SP_CFG_MARK_RXSCR_ERR|mark the carrier error when enable scrambler<br>0: disable "mark the carrier error"<br>1: enable "mark the carrier error"|
|8|SP_CFG_MARK_TXSCR_ERR|mark the carrier error when enable scrambler<br>0: disable "mark the carrier error"<br>1: enable "mark the carrier error"|
|7:4|SP_BYP_START|Scrambler bypass start, which is to generate the scrambler mask, (this function is done for being compatible with old serdes architecture)<br>0 9: to mask the bit position 0 9|
|3:0|SP_BYP_END|Scrambler bypass end, which is to generate the scrambler mask, (this function is done for being compatible with old serdes architecture)<br>0 9: to mask the bit position 0 9|
