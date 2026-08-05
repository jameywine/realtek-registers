---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_AES_KEY_WORD_IND

## Details

*Name* GPON_AES_KEY_WORD_IND

*Offset* 0x703020

*Feature* [AES_DECRYPT](../../feature/AES_DECRYPT)

## Description

AES key word indicator

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15|KEY_WR_REQ|Write request from CPU.|
|14|KEY_WR_COMPL|When the bit is 0x1, it means AES key previous writing operation is complete, CPU can began next operation.|
|13:8|RESERVED||
|7|KEY_USE_IND|0x1: Currently the key bank CPU is operating is the same bank used for decryption. For debug only. Only for debug. Currently this register is not useful.|
|6:3|RESERVED||
|2:0|KEY_WORD_IDX|0x0-0x7, index of AES key words.<br>0x0: correponds to AES-128 key[127:112]<br>0x7: correponds to AES-128 key[15:0]<br>Procedure of configure AES key:<br>1. Write CFG_ACTIVE_KEY: write ’0’ to configure the shadow key and ’1’ to change the currently active key. Please note changing active key would hit the traffic and should never be used during normal operations.<br>2. Write ’0’ then ’1’ to KEY_CFG_REQ to finish writing key<br>3. Write 128-bit key, word-by-word:<br>1) Write KEY_WORD_IDX and the corresponding word (16-bit) to KEY_DATA<br>2) Write ’0’ then ’1’ to KEY_WR_REQ<br>3) Wait until KEY_WR_COMPL = ’1’<br>4) Repeat 1) to 3) for next word until 128-bit key is written.|
