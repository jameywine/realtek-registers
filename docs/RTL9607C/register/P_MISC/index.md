---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: P_MISC

## Details

*Name* P_MISC

*Offset* 0x20004

*Feature* [MAC_CONTROL](../../feature/MAC_CONTROL)

*Bit Offset:* 32

*Port Range:* 0-10

## Description

Register for miscellaneous port stuff.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:26|RESERVED||
|25:24|RESERVED||
|23|DIS_HOLD_BT4IP6||
|22|CFG_RX_FIFO_DIRECT_RST||
|21|CFG_ENBKPRESS|1: Enable back pressure of the port|
|20|RESERVED||
|19|GETTFRD_ORG||
|18|TXCOM_ORG||
|17|PADDING_EN|1: Enable Padding|
|16|BYPS_ABLTY_LOCK||
|15:8|PAD_PAT||
|7|TX_FIRST||
|6|ACCEPT_RX_ERROR||
|5|LATE_COL|0: late collision boundary is at 64 bytes.<br>1: late collision boundary is at 72 bytes.|
|4|SMALL_TAG_IPG|Small IPG for tag insertion.<br>0b0 : No small IPG for tag insertion.<br>0b1 : IPG is reduced by 4 bytes if egress packet length is increased due to tag insertion.|
|3|TX_ITFSP_MODE|TX itfsp monitor source selection between crs and rxdv.<br>0b0 : itfsp monitor source is crs.<br>0b1 : itfsp monitor source is rxdv.|
|2|RX_SPC|enable received special packet which packet length is smaller than 64 bytes, or received packet is not byte alignment and L2 CRC errored packet<br>0b0:disable<br>0b1:enable|
|1|CRC_SKIP|skip L2CRC check<br>0b0:disable<br>0b1:enable|
|0|MAC_LOOPBACK|enable loopback from Tx to Rx in MAC<br>0b0:Disable mac loop-back function<br>0b1:enable mac loop-back function|
