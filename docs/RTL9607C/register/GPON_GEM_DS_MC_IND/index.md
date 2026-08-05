---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GEM_DS_MC_IND

## Details

*Name* GPON_GEM_DS_MC_IND

*Offset* 0x704084

*Feature* [GEM_PORT_DOWNSTREAM](../../feature/GEM_PORT_DOWNSTREAM)

## Description

Downstream GEM block multicast filtering indicator

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15|MC_ITEM_OP_REQ|Write 0x0 then 0x1 to this bit to trigger an operation.|
|14|MC_ITEM_OP_COMPL|0x1: Operation completed, and MC_ITEM_OP_RDATA is updated for reading operation.|
|13|MC_ITEM_OP_HIT|0x1: MC_ITEM_OP_RDATA is valid.|
|12:10|RESERVED||
|9:8|MC_ITEM_OP_MODE|Operation Mode:<br>0b00: no operation<br>0b01: write operation<br>0b10: read operation<br>0b11: clearn operation|
|7:0|MC_ITEM_OP_IDX|Multicast filter item configuration index, 0 255.<br>Multicast Filtering is implemented through CAM. The items of CAM are configured by software by steps:<br>1. Write MC_ITEM_OP_IDX and MC_ITEM_OP_MODE.<br>2. Write MC_ITEM_OP_WDATA if the operation is writing.<br>3. Write ’0’ then ’1’ to MC_ITEM_OP_REQ<br>4. Wait until MC_ITEM_OP_COMPL = ’1’<br>5. If the operation is reading, read MC_ITEM_OP_HIT. If it’s high, go to 6; else there is no match for this index.<br>6. Read MC_ITEM_OP_RDATA.|
