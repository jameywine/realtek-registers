---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: EP_MISC

## Details

*Name* EP_MISC

*Offset* 0x36038

*Feature* [EPON_CONFIGURATION](../../feature/EPON_CONFIGURATION)

## Description

EPON misc configuration register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:8|OE_TX_RECOVER_TIME|epon auto power saving OE recover time|
|7:6|POWER_SAVING_MODE|power saving status|
|5|SRT_GN|Set to 1 by SDK during epon init|
|4|STOP_LOCAL_TIME|Stop local time update, local time will stop<br>0b0:normal operation<br>0b1:local timer will stop update|
|3|RESERVED||
|2|ALWAYS_SVY|1’b1: scan grant list for appropriate next grant all the time<br>1’b0: scan grant list for appropriate next grant only when current grant expired|
|1:0|POWER_SAVING_EN|Enable power saving function<br>0b0:disable<br>0b2:enable|
