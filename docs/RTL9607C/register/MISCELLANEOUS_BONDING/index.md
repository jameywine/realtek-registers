---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: MISCELLANEOUS_BONDING

## Details

*Name* MISCELLANEOUS_BONDING

*Offset* 0x2AC

*Feature* [CHP_INFORMATION](../../feature/CHP_INFORMATION)

## Description

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:6|RESERVED||
|5|BYPS_CLK_LX|When the PAD_DBG_EN=1,<br>Bypass lynx clock ext_clk_lx, input clock from external clock input pin ext_clk_lx<br>0: normal<br>1: bypass ext_clk_lx|
|4|BYPS_CLK_M90|When the PAD_DBG_EN=1,<br>Bypass DDR lag clock ext_clk_m90, input clock from external clock input pin ext_clk_m90<br>0: normal<br>1: bypass ext_clk_m90|
|3|BYPS_CLK_M|When the PAD_DBG_EN=1,<br>Bypass DDR clock ext_clk_m, input clock from external clock input pin ext_clk_m<br>0: normal<br>1: bypass ext_clk_m|
|2|BYPS_CLK_OCP2|When the PAD_DBG_EN=1,<br>Bypass OCP2 clock ext_clk_ocp2, input clock from external clock input pin ext_clk_ocp2 ( PAD_TOD)<br>0: normal<br>1: bypass ext_clk_ocp2|
|1|BYPS_CLK_OCP1|When the PAD_DBG_EN=1,<br>Bypass OCP1 clock ext_clk_ocp1, input clock from external clock input pin ext_clk_ocp1 (PAD_TX_SD)<br>0: normal<br>1: bypass ext_clk_ocp1|
|0|BYPS_CLK_SW|When the PAD_DBG_EN=1,<br>Bypass switch clock ext_clk_sw, input clock from external clock input pin ext_clk_sw (PAD_GTXC)<br>0: normal<br>1: bypass ext_clk_sw|
