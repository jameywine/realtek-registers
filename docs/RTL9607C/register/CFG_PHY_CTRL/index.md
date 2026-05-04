---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: CFG_PHY_CTRL

## Details

*Name* CFG_PHY_CTRL

*Offset* 0x48

*Feature* [INTERFACE](../../feature/INTERFACE)

## Description

Config for phyad and broadcast mode

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:10|RESERVED||
|9:5|MSK_MDI|mask the specific gphy’s mdi|
|4:0|BASE_PHYAD|start phyad for SMI. phy0_ad=N, phy1_ad=N+1, , phy4_ad=N+4|
