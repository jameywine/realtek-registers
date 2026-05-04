---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: IOPAD_CFG

## Details

*Name* IOPAD_CFG

*Offset* 0x30

*Feature* [INTERFACE](../../feature/INTERFACE)

## Description

IO pad config for dirving, slew rate, and DP, DN, 3.3V for RGMII

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:27|RESERVED||
|26:24|RG_DP|adjust PMOS resistance for RGMII TX PAD which is inverse proportion to this setting.|
|23:21|RG_DN|adjust NMOS resistance for RGMII TX PAD which is inverse proportion to this setting.|
|20|RG_SEL33|1: 3.3v RGMII PAD|
|19|DRI_LED|1: high dirving|
|18|DRI_EXT_CK|1: high dirving|
|17|DRI_EXT_DT|1: high dirving|
|16|DRI_IFCK|1: high dirving|
|15|DRI_IFDT|1: low slew rate|
|14|DRI_SLIC_CK|1: high dirving|
|13|DRI_SLIC_DT|1: high dirving|
|12|DRI_SPI_CK|1: high dirving|
|11|DRI_SPI_DT|1: high dirving|
|10|DRI_OTH|1: high dirving|
|9|SR_EXT_CK|1: low slew rate|
|8|SR_EXT_DT|1: low slew rate|
|7|SR_IFCK|1: low slew rate|
|6|SR_IFDT|1: low slew rate|
|5|SR_SLIC_CK|1: low slew rate|
|4|SR_SLIC_DT|1: low slew rate|
|3|SR_LED|1: low slew rate|
|2|SR_SPI_CK|1: low slew rate|
|1|SR_SPI_DT|1: low slew rate|
|0|SR_OTH|1: low slew rate|
