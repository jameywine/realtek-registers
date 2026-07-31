---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: SDS_REG14

## Details

*Name* SDS_REG14

*Offset* 0x40838

*Feature* [PHY_SERDES](../../feature/PHY_SERDES)

## Description

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15|SP_CFG_SPDUP|when asserted high, the timer inside sds_port will be put into speed-up mode (for simulation usage)|
|14|SP_CFG_SPDUP_FIB100||
|13|SP_CFG_RXSLEEP_TMROUT||
|12|SP_SEL_CALIBOK||
|11|SP_SEL_SDET||
|10|SP_SEL_ANOK||
|9|SP_CFG_SEL_ODD_BIT|select cma_det operating on half_rate mode|
|8|SP_CFG_FRC_LD_VALUE|sds_frc_ld value in force mode<br>1’b1: sds_frc_ld high<br>1’b0: sds_frc_ld low|
|7|SP_CFG_FRC_LD|select sds_frc_ld control in force mode<br>1’b0: sds_frc_ld driven by input<br>1’b1: sds_frc_ld driven by cfg_frc_ld_value|
|6|SP_CFG_SGMI_CK1MS_EN||
|5:3|SP_CFG_LINK_TMR_SGMII_SEL||
|2:0|SP_CFG_LINK_TMR_NORM_SEL|select link_timer_done (not SGMII)<br>3’d0: 8ms<br>3’d1: 9ms<br>3’d2: 10ms<br>3’d3: 11ms<br>3’d4: 12ms<br>3’d5: 13ms<br>3’d6: 14ms<br>3’d7: 16ms|
