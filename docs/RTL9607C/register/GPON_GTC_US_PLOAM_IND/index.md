---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GTC_US_PLOAM_IND

## Details

*Name* GPON_GTC_US_PLOAM_IND

*Offset* 0x7050C0

*Feature* [GTC_UPSTREAM](../../feature/GTC_UPSTREAM)

## Description

PLOAMu indication

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:11|RESERVED||
|10:8|PLM_TYPE|PLOAMu type:<br>0b000: Normal PLOAMu<br>0b001: Urgent PLOAMu<br>0b101: Dying Gasp PLOAMu<br>0b110: SN PLOAMu<br>0b111: US_NOMSG PLOAMu|
|7|PLM_NRM_EMPTY|0x1: Normal PLOAMu buffer is empty.|
|6|PLM_NRM_FULL|0x1: Normal PLOAMu buffer is full.|
|5|PLM_URG_EMPTY|0x1: Urgent PLOAMu buffer is empty.|
|4|PLM_URG_FULL|0x1: Urgent PLOAMu buffer is full.|
|3:1|RESERVED||
|0|PLM_ENQ|PLOAMu write Refresh. CPU write 0x0 then 0x1 to this bit to push the written message to buffer.<br>Software writes PLOAMu messages to message buffer following the procedure:<br>1. Write PLM_TYPE<br>2. Wait PLM_URG_FULL = ’0’ when software try to write urgent PLOAMu; Wait PLM_NRM_FULL = ’0’ when software try to write normal PLOAMu.<br>3. Write message data to PLM_DATA<br>4. Write ’0’ then ’1’ to PLM_ENQ<br>5. If software has more messages to write, go back to Step 1.|
