---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: SW_PWRSAV_CTRL

## Details

*Name* SW_PWRSAV_CTRL

*Offset* 0x2CC

*Feature* [POWER_SAVING](../../feature/POWER_SAVING)

## Description

swcore power saving control

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:19|RESERVED||
|18|SLOW_DOWN_PLL_EN|slow down PLL as swcore power saving|
|17|SLOW_DOWN_CLK_EN|slow down swcore clock as swcore power saving|
|16|FRC_MAC_ACTIVE|active MAC port force mode|
|15:12|SLOW_CLK_TGL_RATE|dgckmx cks clock source|
|11:2|GPHY_MDX_MDC_DIV|GPHY MDC freq division|
|1|WAIT_FOR_AGREEMENT|swcore power saving need CPU agreement|
|0|AGREE_SLEEP|agree swcore power saving|
