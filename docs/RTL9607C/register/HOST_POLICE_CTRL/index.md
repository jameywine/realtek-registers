---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: HOST_POLICE_CTRL

## Details

*Name* HOST_POLICE_CTRL

*Offset* 0x1C11C

*Feature* [STORM_CONTROL_B_M_UM_DLF_](../../feature/STORM_CONTROL_B_M_UM_DLF_)

*Bit Offset:* 64

*Array Range:* 0-31

## Description

Host bandwidth control.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|63|RESERVED||
|62|CNT_EN|state of host statistic counting function.<br>0: disable.<br>1: enable.|
|61:56|POLICE_SA_METER|shared meter of host bandwith control|
|55|POLICE_SA_EN|state of host ingress bandwidth control<br>0: disable.<br>1: enable.|
|54:49|POLICE_DA_METER|shared meter of host bandwith control|
|48|POLICE_DA_EN|state of host egress bandwidth control<br>0: disable.<br>1: enable.|
|47:40|MAC5|MAC address 5|
|39:32|MAC4|MAC address 4|
|31:24|MAC3|MAC address 3|
|23:16|MAC2|MAC address 2|
|15:8|MAC1|MAC address 1|
|7:0|MAC0|MAC address 0|
