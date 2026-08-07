---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: SWPBO_IO_CMD_1

## Details

*Name* SWPBO_IO_CMD_1

*Offset* 0xF15438

*Feature* [SWPBO_NIC_CPU_IF](../../feature/SWPBO_NIC_CPU_IF)

## Description

switch PBO PONNIC IO Command 1 Register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:28|RESERVED||
|27|PRECISE_DMA_EN||
|26|RESERVED||
|25|R_EN_RX_MRING|Enable rx multiple rings.<br>1: rx using multiple rings.<br>0. rx using single ring.|
|24|GB_EN||
|23:18|RESERVED||
|17|R_SET_RX_P9QFLAG||
|16|R_SET_RX_P8QFLAG||
|15|R_SET_RX_P7QFLAG||
|14|R_SET_RX_P6QFLAG||
|13|R_SET_RX_P5QFLAG||
|12|R_SET_RX_P4QFLAG||
|11|R_SET_RX_P3QFLAG|Ring3 enable|
|10|R_SET_RX_P2QFLAG|Ring2 enable|
|9|R_SET_RX_P1QFLAG|Ring1 enable|
|8|R_SET_RX_P0QFLAG|Ring0 enable|
|7:6|RESERVED||
|5:4|R_RPAGE_SIZE|switch PBO PONNIC Rx page size.<br>0: 128B<br>1: 256B<br>2: 512B|
|3:2|RESERVED||
|1:0|R_TPAGE_SIZE|switch PBO PONNIC Tx page size.<br>0: 128B<br>1: 256B<br>2: 512B|
