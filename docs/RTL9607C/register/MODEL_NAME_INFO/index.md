---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: MODEL_NAME_INFO

## Details

*Name* MODEL_NAME_INFO

*Offset* 0x10000

*Feature* [CHP_INFORMATION](../../feature/CHP_INFORMATION)

## Description

Specify the model name information.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RTL_ID|RTL number|
|15:11|MODEL_CHAR_1ST|First English character of model name<br>0x0: NULL character<br>0x1-0x1A: character A - Z<br>0x1B-0x1F: invalid|
|10:6|MODEL_CHAR_2ND|Second English character of model name<br>0x0: NULL character<br>0x1-0x1A: character A - Z<br>0x1B-0x1F: invalid|
|5:4|MODEL_CHAR_3RD|Dummy Field|
|3:0|RTL_VID|RTL Revision ID|
