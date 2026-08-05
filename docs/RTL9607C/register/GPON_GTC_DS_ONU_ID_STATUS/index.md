---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GTC_DS_ONU_ID_STATUS

## Details

*Name* GPON_GTC_DS_ONU_ID_STATUS

*Offset* 0x701010

*Feature* [GTC_DOWNSTREAM](../../feature/GTC_DOWNSTREAM)

## Description

ONU Identifier and status

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15:8|ONU_ID|ONU Identifier. Used to filter received PLOAMd message and BWMap allocations. Should be set to 0xFF before ranging, and changed to the real ONUID assigned by OLT.|
|7:4|RESERVED||
|3:0|ONU_STATE|ONU State Coding.<br>0x0: unknown state<br>0x1: O1 state<br>0x2: O2 state<br>0x3: O3 state<br>0x4: O4 state<br>0x5: O5 state<br>0x6: O6 state<br>0x7: O7 state|
