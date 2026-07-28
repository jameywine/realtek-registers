---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: CPU_PLL_CTRL_DUMMY

## Details

*Name* CPU_PLL_CTRL_DUMMY

*Offset* 0x354

*Feature* [OTHER](../../feature/OTHER)

## Description

CPU PLL Control
Used by _rtl9607c_lan_sds0_modeV3_set() and _rtl9607c_lan_sds1_modeV3_set(s)

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:30|SPDSEL_SGMII_USB3|APHY speed mode selection for Serde port 6<br>1: PLL/2<br>1: PLL/4|
|29|SGMII_SEL_USB3|1: Fiber 1G, SGMII<br>0: HiSGMII, 2500BaseX|
|28:27|SPDSEL_SGMII_PCIE|APHY speed mode selection for Serde port 7<br>1: PLL/2<br>1: PLL/4|
|26|SGMII_SEL_PCIE|1: Fiber 1G, SGMII<br>0: HiSGMII, 2500BaseX|
|25:0|PLL_DUMMY||
