---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: SDS_REG2

## Details

*Name* SDS_REG2

*Offset* 0x40808

*Feature* [PHY_SERDES](../../feature/PHY_SERDES)

## Description

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15:14|SP_FRC_PREAMBLE|force insert preamble for solving the lose preamble issue<br>frc_preamble[0] = 1’b0: auto mode<br>frc_preamble[0] = 1’b1: force mode, the force value is frc_preamble[1]|
|13:12|SP_FRC_IPG|force insert IPG for solving the lose preamble issue<br>frc_ipg[0] = 1’b0: auto mode<br>frc_ipg[0] = 1’b1: force mode, the force value is frc_ipg[1]|
|11:10|SP_FRC_CGGOOD|force code-group good<br>frc_cggoo{0} = 1’b0: auto mode<br>frc_cggood{0} = 1’b1: force mode, the force value is frc_cggood{1}|
|9:8|SP_SDS_FRC_AN|serdes force N-way enable/disable<br>sds_frc_an{0} = 1’b0: auto mode<br>sds_frc_an{0} = 1’b1: force mode, the force value is sds_frc_an{1}|
|7|SP_CFG_INS_IPG_MDY||
|6|SP_CFG_RDS_CMA_DET||
|5:4|SP_CFG_SEL_TMR_LIM||
|3:0|SP_SDS_RESTART_AN|serdes restart N-way for 4-port<br>0: normal<br>1: restart N-way|
