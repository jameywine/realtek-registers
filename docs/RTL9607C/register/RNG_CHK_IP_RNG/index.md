---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: RNG_CHK_IP_RNG

## Details

*Name* RNG_CHK_IP_RNG

*Offset* 0x15294

*Feature* [RANGE_CHECK_PORT_VLAN_IP_L4PORT_](../../feature/RANGE_CHECK_PORT_VLAN_IP_L4PORT_)

*Bit Offset:* 288

*Array Range:* 0-15

## Description

IP range check configuration

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|287:259|RESERVED||
|258:256|TYPE|Range checking data type<br>0:non-valid<br>1:IPv4 SIP range check<br>2:IPv4 DIP range check<br>3:IPv6 SIP{31:0} range check<br>4:IPv6 DIP{31:0} range check<br>5 7:reserved|
|255:224|IP_UPPER_127_96|P range check upper bound IP|
|223:192|IP_UPPER_95_64|P range check upper bound IP|
|191:160|IP_UPPER_63_32|P range check upper bound IP|
|159:128|IP_UPPER_31_0|P range check upper bound IP|
|127:96|IP_LOWER_127_96|IP range check lower bound IP|
|95:64|IP_LOWER_95_64|IP range check lower bound IP|
|63:32|IP_LOWER_63_32|IP range check lower bound IP|
|31:0|IP_LOWER_31_0|IP range check lower bound IP|
