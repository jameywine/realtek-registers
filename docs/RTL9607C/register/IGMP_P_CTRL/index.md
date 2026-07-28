---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: IGMP_P_CTRL

## Details

*Name* IGMP_P_CTRL

*Offset* 0x11098

*Feature* [IGMP_SNOOPING](../../feature/IGMP_SNOOPING)

*Bit Offset:* 32

*Port Range:* 0-10

## Description

IGMP snooping per-port control

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:11|RESERVED||
|10|ALLOW_MC_DATA|Allow Multicast Data<br>1: Allow<br>0: Drop|
|9:8|MLDV2_OP|MLDv2 operation control<br>0b00: Flooding<br>0b01: Drop<br>0b10: Trap to CPU<br>0b11: Reserved|
|7:6|MLDV1_OP|MLDv1 operation control<br>0b00: Flooding<br>0b01: Drop<br>0b10: Trap to CPU<br>0b11: Reserved|
|5:4|IGMPV3_OP|IGMPv3 operation control<br>0b00: Flooding<br>0b01: Drop<br>0b10: Trap to CPU<br>0b11: Reserved|
|3:2|IGMPV2_OP|IGMPv2 operation control<br>0b00: Flooding<br>0b01: Drop<br>0b10: Trap to CPU<br>0b11: Reserved|
|1:0|IGMPV1_OP|IGMPv1 operation control<br>0b00: Flooding<br>0b01: Drop<br>0b10: Trap to CPU<br>0b11: Reserved|
