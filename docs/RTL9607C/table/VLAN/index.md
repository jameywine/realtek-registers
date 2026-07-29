---
tags:
  - RTL9607C
  - Table
  - Table Fields
---

# RTL9607C table: VLAN

## Details

*Name* VLAN

*Feature* [TABLE_ACCESS](../../feature/TABLE_ACCESS)

*Type* 1

*Entries* 4096

*Control register* [TBL_ACCESS_CTRL](../../register/TBL_ACCESS_CTRL)

*Write Data register* [TBL_ACCESS_WR_DATA](../../register/TBL_ACCESS_WR_DATA)

*Read Data register* [TBL_ACCESS_RR_DATA](../../register/TBL_ACCESS_RR_DATA)

## Description

VLAN Table

## Fields

|Name|LSB|Bits|Description|
| :--- | :--- | :--- | :--- |
|EXT_MASKIDX|26|5|extension mask index?|
|IVL_SVL|25|1|IVL=1 or SVL=0|
|SVLAN_CHK_IVL_SVL|24|1||
|FID_MSTI|22|2|FID or MSTI|
|UNTAG|11|11|untag set|
|MBR|0|11|VLAN member|
