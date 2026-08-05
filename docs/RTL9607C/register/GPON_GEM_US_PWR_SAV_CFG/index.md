---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GEM_US_PWR_SAV_CFG

## Details

*Name* GPON_GEM_US_PWR_SAV_CFG

*Offset* 0x706024

*Feature* [GEM_UPSTREAM](../../feature/GEM_UPSTREAM)

## Description

GEM upstream Power Saving configuration

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31|USE_TX_OPT_DISABLE||
|30:21|RESERVED||
|20:16|OPT_BEHIND_CYCLES|Set to 0x10 by SDK during gpon init|
|15:10|RESERVED||
|9:0|OPT_AHEAD_CYCLES|Set to 0x100 by SDK during gpon init|
