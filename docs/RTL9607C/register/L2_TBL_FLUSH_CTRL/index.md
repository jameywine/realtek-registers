---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: L2_TBL_FLUSH_CTRL

## Details

*Name* L2_TBL_FLUSH_CTRL

*Offset* 0x17044

*Feature* [ADDRESS_LEARNING_FLUSH](../../feature/ADDRESS_LEARNING_FLUSH)

## Description

L2 table flush control register. Specify the fid/vid and/or port to flush entries or replace the SLP field of L2 table.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:19|RESERVED||
|18:17|LUT_FLUSH_FID|L2 flushing FID|
|16:5|LUT_FLUSH_VID|L2 flushing VID|
|4|LUT_FLUSH_DYNAMIC|enable Force Flush dynamic entries|
|3|LUT_FLUSH_STATIC|enable Force Flush static entries|
|2:1|LUT_FLUSH_MODE|Force lut flush mode 0b00: Port based<br>0b01: Port + VLAN based<br>0b10: Port + FID/MSTI based<br>0b11:reserved.|
|0|FLUSH_STATUS|Status of flush L2 table action.<br>0: non-busy<br>1: busy|
