---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: STAT_L34_FLOW_RST

## Details

*Name* STAT_L34_FLOW_RST

*Offset* 0x34044

*Feature* [OTHER](../../feature/OTHER)

*Bit Offset:* 1

*Array Range:* 0-31

## Description

Flow MIB Stat Reset
Array Range corresponds to index of Flow MIB table
Used by rtk_rg_asic_flowMib_reset()

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|0|EN|Write 1 here and to RST_CMD bit of STAT_RST_CFG register to initiate a reset and then wait for BUSY_STAT of STAT_RST_CFG register. Then write 0 to clear reset request by manual.|
