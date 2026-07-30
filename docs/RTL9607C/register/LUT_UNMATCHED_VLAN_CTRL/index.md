---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: LUT_UNMATCHED_VLAN_CTRL

## Details

*Name* LUT_UNMATCHED_VLAN_CTRL

*Offset* 0x1C008

*Feature* [ADDRESS_TABLE_LOOKUP](../../feature/ADDRESS_TABLE_LOOKUP)

*Bit Offset:* 1

*Port Range:* 0-10

## Description

unmatched VLAN control register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|0|ACT|forwarding action when vid learning unmatch happen on specified port.<br>0: Forward.<br>1: Trap to CPU.|
