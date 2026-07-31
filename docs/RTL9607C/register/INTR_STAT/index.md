---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: INTR_STAT

## Details

*Name* INTR_STAT

*Offset* 0x1D014

*Feature* [INTERRUPT](../../feature/INTERRUPT)

*Bit Offset:* 64

## Description

Interrupt status

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|63:60|INTR_STAT_THERMAL||
|59:53|RESERVED||
|52:48|INTR_STAT_GPHY|Per gphy interrupted|
|47:43|RESERVED||
|42:32|INTR_STAT_PORT_LINKDOWN|Per port had been link down state|
|31:27|RESERVED||
|26:16|INTR_STAT_PORT_LINKUP|Per port had been link up state|
|15:11|RESERVED||
|10:0|INTR_STAT_PORT_CHANGE|Per-port link speed changed statusM<br>0:not changed<br>0b1:changed|
