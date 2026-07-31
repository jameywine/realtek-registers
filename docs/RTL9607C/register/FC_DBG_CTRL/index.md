---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: FC_DBG_CTRL

## Details

*Name* FC_DBG_CTRL

*Offset* 0x2D038

*Feature* [FLOWCONTROL_BACKPRESSURE_THRESHOLD](../../feature/FLOWCONTROL_BACKPRESSURE_THRESHOLD)

## Description

Flow control tuning debug control

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:15|RESERVED||
|14|PAUSE_OFF_ORG_EN||
|13:10|PORT_NO|Port number of flow control debugging information latching register address from ????|
|9|CLR_TOTAL_PKTCNT||
|8|CLR_PE_MAX_PAGE_CNT|Clear maximum egress port latch page value|
|7:0|CLR_Q_MAX_PAGE_CNT|Clear maximum egress queue latch page value|
