---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: SDS_REG4

## Details

*Name* SDS_REG4

*Offset* 0x40810

*Feature* [PHY_SERDES](../../feature/PHY_SERDES)

## Description

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15:13|SP_CFG_FRC_SDS_MODE|force sds_mode enable<br>3’d3: fib1g<br>3’d5: fib100<br>3’d7: fib100/fib1g auto_det|
|12|SP_CFG_FRC_SDS_MODE_EN|force sds_mode enable|
|11:8|SP_CFG_UPD_RXD|control the sample point of crxd(from codec_8b10b) to grxd(gmii)<br>4’d3: sample crxd 24ns later (after crxd transiton)|
|7:4|SP_CFG_UPD_TXD|control the sample point of gtxd(gmii) to ctxd(to codec_8b10b)<br>4’d4: sample gtxd 32ns later (after gtxd transiton)|
|3|SP_CFG_UPD_RXD_DYN|1’b1: rate_adpt update rxd dynamic<br>1’b0: rate_adpt update rxd according to cfg_upd_rxd|
|2|SP_CFG_EN_LINK_FIB1G|fix one_giga disable N-way linkon issue|
|1|SP_CFG_EN_LINK_SGM|fix one_giga disable N-way linkon issue|
|0|SP_CFG_SGM_CK_SEL|modify sgmii clock select|
