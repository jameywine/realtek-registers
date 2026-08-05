---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GTC_DS_INTR_MASK

## Details

*Name* GPON_GTC_DS_INTR_MASK

*Offset* 0x701004

*Feature* [GTC_DOWNSTREAM](../../feature/GTC_DOWNSTREAM)

## Description

GTC downstream interrupt mask

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:12|RESERVED||
|11|PPS_M||
|10|PLM_BUF_M|0x0: PLM_BUF_REQ can not generate inrerrupt.<br>0x1: PLM_BUF_REQ can generate inrerrupt.|
|9|RNG_REQ_M|x0: RNG_REQ_HIS can not generate inrerrupt.<br>0x1: RNG_REQ_HIS can generate inrerrupt.|
|8|SN_REQ_M|0x0: SN_REQ_HIS can not generate inrerrupt.<br>0x1: SN_REQ_HIS can generate inrerrupt.|
|7:4|RESERVED||
|3|LOM_M|0x0: LOM_DLT can not generate inrerrupt.<br>0x1: LOM_DLT can generate inrerrupt.|
|2|DS_FEC_STA_M|0x0: DS_FEC_STA_DLT can not generate inrerrupt.<br>0x1: DS_FEC_STA_DLT can generate inrerrupt.|
|1|LOF_M|0x0: LOF_DLT can not generate inrerrupt.<br>0x1: LOF_DLT can generate inrerrupt.|
|0|LOS_M|0x0: LOS_DLT can not generate inrerrupt.<br>0x1: LOS_DLT can generate inrerrupt.|
