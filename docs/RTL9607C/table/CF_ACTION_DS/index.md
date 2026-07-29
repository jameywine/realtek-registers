---
tags:
  - RTL9607C
  - Table
  - Table Fields
---

# RTL9607C table: CF_ACTION_DS

## Details

*Name* CF_ACTION_DS

*Feature* [TABLE_ACCESS](../../feature/TABLE_ACCESS)

*Type* 5

*Entries* 256

*Control register* [TBL_ACCESS_CTRL](../../register/TBL_ACCESS_CTRL)

*Write Data register* [TBL_ACCESS_WR_DATA](../../register/TBL_ACCESS_WR_DATA)

*Read Data register* [TBL_ACCESS_RR_DATA](../../register/TBL_ACCESS_RR_DATA)

## Description

Classification downstrean action control table

## Fields

|Name|LSB|Bits|Description|
| :--- | :--- | :--- | :--- |
|CF_PRI|61|3|Assigned classification priority|
|CFPRI_ACT|60|1|Classification priority assignment for packets<br>0b0:Internal priority follow switch core<br>0b1:Forced internal priority to CFPRI|
|CPRI_ACT|57|3|Assigned classification priority action|
|CVID_ACT|54|3|Assigned C tag VID action|
|C_PRI|51|3|Assigned C tag P-bits|
|C_VID|39|12|Assigned C tag VID|
|CACT|37|2|0b00:nop<br>0b01:C-tagging(TPID 0x8100)<br>0b10:Enable VLAN translation with SP2C table(Keep ingress tag TPID)<br>0b11: Transparent(ingnore VLAN egress filtering and keep egress Ctag format with the same ingress tag TPID)|
|UNI_ACT|35|2|Forced forward port mask action<br>0b0: forwarding member mask to UNI_MASK only<br>0b1: assign UNI_MASK to forced forwarding<br>Other: unknown|
|UNI_PMSK|24|11|forced forward/flooding port mask|
|CSVID_ACT|21|3|0b00: Assigned to VID<br>0b01: Copy from 1st tag VID<br>0b10: Copy from 2nd tag VID<br>Other:reserved/unknown|
|CSPRI_ACT|18|3|0b00: Assigned to CSPRI<br>0b01: Copy from 1st tag P-bits<br>0b10: Copy from 2nd tag P-bits<br>0b11: Assign from internal priority<br>Other: unknown?|
|CS_PRI|15|3|Assigned S tag P-bits|
|CS_VID|3|12|Assigned S tag VID|
|CSACT|0|3|0b000:nop(follow switch-core)<br>0b001:add classification tag which TPID as VS_TPID (reference to CSVID_ACT/CSPRI_ACT)<br>0b010:add classification tag which TPID as 0x8100 (reference to CSVID_ACT/CSPRI_ACT)<br>0b011:delete Stag<br>0b100: transparent<br>0b101: Enable VLAN translation with SP2C table with 1st tag VID(both unmath and unhit will un-Stag)<br>Other: reserved|
