---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: CFG_UNHIOL

## Details

*Name* CFG_UNHIOL

*Offset* 0x23104

*Feature* [MAC_CONTROL](../../feature/MAC_CONTROL)

## Description

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:10|RESERVED||
|9|DIS_ITFSP_OP|1: disable itfsp|
|8|DIS_SKIP_FP|dis skip fp|
|7:5|ITFSP_REG|select tx ipg<br>00:0byte<br>01:1byte<br>10:2byte|
|4|IOL_16DROP|iol drop, drop packet after 16 collisions|
|3|IOL_BACKOFF|the iol mode backoff, using full 10-bits|
|2|BACKOFF_RANDOM_TIME|only using 3-bits for backoff random timer|
|1|DISABLE_BACK_OFF|Dont do back off<br>priority : disbkoff > spdbkoff > unhbkoff > normal bkoff(9 bits)|
|0|IPG_COMPENSATION|0:90ppm TX IPG compensation<br>1:65ppm TX IPG compensation|
