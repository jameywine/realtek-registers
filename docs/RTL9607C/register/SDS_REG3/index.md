---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: SDS_REG3

## Details

*Name* SDS_REG3

*Offset* 0x4080C

*Feature* [PHY_SERDES](../../feature/PHY_SERDES)

## Description

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15|SP_WR_SOFT_RSTB|write software soft-reset<br>0: normal<br>1: write soft-reset, write 8 times then trigger software soft-reset|
|14|SP_USE_25M_CLK|When CMU_EN = 1’b0, MAC gtxc/grxc will be zero, we can let gtxc/grxc be a free-run 25MHz clock<br>0: gtxc/grxc no clock when CMU_EN = 1’b0<br>1: gtxc/grxc is 25MHz when CMU_EN = 1’b0|
|13|SP_MARK_CARR_EXT|mark the carrier extend error issue, e2s_d0 = 10’h20f will be marked as 10’h00f|
|12|SP_SEL_DEG|select deglich circuit for e2s_ck and s2e_ck<br>0: without deglich circuit<br>1: with deglich circuit|
|11:8|SP_REG_CALIB_OK_CNT|U55 serdes IP will not support "CALIB_OK" to indicate that the CLKWR is ready, so we generate "CALIB_OK" by ourself. The signal will be generated after negedge of "RXIDLE" X us. The X is defined as follows.<br>0: calib_ok always 1’b1<br>1 15: calib_ok is delay|
|7|SP_EXT_PWR_CTL|CMU_EN/PDOWN/ the power saving related control<br>0: will be affected by sds_frc_ld, sds_en_rx, sds_en_tx<br>1: will not be affected|
|6|SP_SOFT_RST|level software-reset<br>0: normal<br>1: do level software-reset|
|5|SP_CLR_SOFT_RSTB|clear software soft-reset, soft-reset need the write soft-reset counter to be 8 timer, clear soft-reset means to clear the soft-reset counter<br>0: normal<br>1: clear the soft-reset counter|
|4:0|SP_CMA_RQ|number of comma should be received for alignment|
