---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: NAT_TBL_ACCESS_CLR

## Details

*Name* NAT_TBL_ACCESS_CLR

*Offset* 0x801104

*Feature* [TABLE_ACCESS](../../feature/TABLE_ACCESS)

## Description

NAT Table Access Clear register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:13|RESERVED||
|12|RST_TCAM_TBL|Trigger hardware to quickly reset tcam table . Also means status.<br>0b0: completed<br>0b1: executing<br>(Note:Set it with 1 to perform command. When hardware completes the table reset, it will clear this bit. )|
|11|RESERVED||
|10|RST_MAC_INDEX_TBL|Trigger hardware to quickly reset mac_index table . Also means status.<br>0b0: completed<br>0b1: executing<br>(Note:Set it with 1 to perform command. When hardware completes the table reset, it will clear this bit. )|
|9|RST_CAM_TBL|Trigger hardware to quickly reset cam table . Also means status.<br>0b0: completed<br>0b1: executing<br>(Note:Set it with 1 to perform command. When hardware completes the table reset, it will clear this bit. )|
|8|RST_FLOW_TBL|Trigger hardware to quickly reset flow table . Also means status.<br>0b0: completed<br>0b1: executing<br>(Note:Set it with 1 to perform command. When hardware completes the table reset, it will clear this bit. )|
|7:5|RESERVED||
|4|RST_WAL_TBL|Trigger hardware to quickly reset wan access limit table . Also means status.<br>0b0: completed<br>0b1: executing<br>(Note:Set it with 1 to perform command. When hardware completes the table reset, it will clear this bit. )|
|3|RST_EXT_PORT|Trigger hardware to quickly reset ext_port table . Also means status.<br>0b0: completed<br>0b1: executing<br>(Note:Set it with 1 to perform command. When hardware completes the table reset, it will clear this bit. )|
|2|RESERVED||
|1|RST_ETHER_TYPE|Trigger hardware to quickly reset ethertype table . Also means status.<br>0b0: completed<br>0b1: executing<br>(Note:Set it with 1 to perform command. When hardware completes the table reset, it will clear this bit. )|
|0|RST_IF_TBL|Trigger hardware to quickly reset interface table . Also means status.<br>0b0: completed<br>0b1: executing<br>(Note:Set it with 1 to perform command. When hardware completes the table reset, it will clear this bit. )|
