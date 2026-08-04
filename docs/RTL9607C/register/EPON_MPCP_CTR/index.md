---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: EPON_MPCP_CTR

## Details

*Name* EPON_MPCP_CTR

*Offset* 0x3609C

*Feature* [EPON_CONFIGURATION](../../feature/EPON_CONFIGURATION)

## Description

EPON mpcp control register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:5|RESERVED||
|4:3|GATE_TRAP_TYPE||
|2|OTHER_HANDLE|mpcp packet for this EPON MAC but opcode is not Gate or Register<br>0b0 Drop<br>0b1 Pass|
|1|GATE_HANDLE|0b0 ASIC Handle<br>0b1 ASIC Handle and trap to CPU|
|0|INVALID_LEN_HANDLE|mpcp packet for this EPON MAC but length is not 64 byte<br>0b0 Drop<br>0b1 Pass|
