---
tags:
  - RTL9607C
  - Table
  - Table Fields
---

# RTL9607C table: CF_RULE_T0

## Details

*Name* CF_RULE_T0

*Feature* [TABLE_ACCESS](../../feature/TABLE_ACCESS)

*Type* 4

*Entries* 256

*Control register* [TBL_ACCESS_CTRL](../../register/TBL_ACCESS_CTRL)

*Write Data register* [TBL_ACCESS_WR_DATA](../../register/TBL_ACCESS_WR_DATA)

*Read Data register* [TBL_ACCESS_RR_DATA](../../register/TBL_ACCESS_RR_DATA)

## Description

Classification rule data table 0

## Fields

|Name|LSB|Bits|Description|
| :--- | :--- | :--- | :--- |
|VALID|48|1|valid bit|
|INTER_PRI|45|3|Internal priority|
|PPPOE|44|1|PPPoE packet?|
|IPV4|43|1|IPv4 packet?|
|IPV6|42|1|IPv6 packet?|
|IPMC|41|1|IP multicast packet ?|
|IGMP_MLD|40|1|IGMP/MLD control packet ?|
|ACL_HIT|32|8|ACL hit check|
|U_D|31|1|Rule of upstream or downstream<br>0b0:upstream<br>0b1:downstream|
|TOS_GEMIDX|23|8|Upstream TOS or downstream GEMIDX or LLID|
|OUTER_TAG|7|16||
|STPID|6|1||
|IF_STAG|5|1|has S-tag|
|IF_CTAG|4|1|has C-tag|
|UNI|0|4|UNI/UTP port|
