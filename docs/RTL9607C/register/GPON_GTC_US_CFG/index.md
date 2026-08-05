---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GTC_US_CFG

## Details

*Name* GPON_GTC_US_CFG

*Offset* 0x705014

*Feature* [GTC_UPSTREAM](../../feature/GTC_UPSTREAM)

## Description

GTC upstream configuration. The register is protected.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15|FS_LON|0x1: Force turning on optical transmission when FS_LOFF is zero.|
|14|FS_LOFF|0x1: Force turning off optical transmission.|
|13:12|RESERVED||
|11|LESS_RANDOM||
|10|IND_NRM_PLM|0x0: IND[7] is set only when urgent PLOAMu waiting.<br>0x1: IND[7] is set when any PLOAMu waiting|
|9|PLM_DIS|0x1: Disable sending PLOAMu to OLT. If PLOAMu is requested by BWMap, US_NOMSG will be send.|
|8|DBRU_DIS|0x1: Disable sending DBRu to OLT. If PLOAMu is requested by BWMap, all 0 will be send.|
|7:5|RESERVED||
|4|ENA_AUTO_DG|0x0: Disable sending Dying Gasp message automatically.<br>0x1: Eisable sending Dying Gasp message automatically|
|3|US_BEN_POLAR|The polarity of burst control.<br>0x0: Low to enable laser transmission<br>0x1: High to enable laser transmission|
|2:1|RESERVED||
|0|SCRM_DIS|0x1: Disable scrambling in upstream.|
