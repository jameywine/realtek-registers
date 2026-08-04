---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: LLID_TABLE

## Details

*Name* LLID_TABLE

*Offset* 0x3603C

*Feature* [EPON_CONFIGURATION](../../feature/EPON_CONFIGURATION)

*Bit Offset:* 96

*Array Range:* 0-7

## Description

LLID table Register. The RS layer will accept the LLID list in this table.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|95:81|RESERVED||
|80|MONITOR_MODE||
|79:72|ONU_MAC5|EPON registeration MAC address 5|
|71:64|ONU_MAC4|EPON registeration MAC address 4|
|63:56|ONU_MAC3|EPON registeration MAC address 3|
|55:48|ONU_MAC2|EPON registeration MAC address 2|
|47:40|ONU_MAC1|EPON registeration MAC address 1|
|39:32|ONU_MAC0|EPON registeration MAC address 0|
|31:23|RESERVED||
|22|REPORT_TIMEOUT|Indicator report timer is timeout, this bit will set to 1. When report packet send out this bit will set to 0.|
|21:16|REPORT_TIMER|Record the report age value.<br>Unit 10ms<br>Set the value to 0 is disable this timer.|
|15|VALID|Valid bit.<br>0b0: this LLID is invalid.<br>0b1: this LLID is valid.|
|14:0|LLID|This field record the LLID|
