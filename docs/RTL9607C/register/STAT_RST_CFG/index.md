---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: STAT_RST_CFG

## Details

*Name* STAT_RST_CFG

*Offset* 0x3401C

*Feature* [STATISTIC_COUNTERS](../../feature/STATISTIC_COUNTERS)

## Description

MIB reset configurations

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:7|RESERVED||
|6|BUSY_STAT|Busy status for reset operation|
|5|RST_CMD|Reset MIB and counter (clear by ASIC)|
|4:2|RST_LLID_IDX|LLID table index|
|1|RST_LLID|Reset the specified LLID index counters|
|0|RST_EPON_MIB|Reset EPON global counters|
