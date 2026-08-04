---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: EPON_RDM_SEED

## Details

*Name* EPON_RDM_SEED

*Offset* 0x36180

*Feature* [EPON_CONFIGURATION](../../feature/EPON_CONFIGURATION)

## Description

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15:0|EPON_RDM_SEED|Set to 0 by SDK for "init discovery random seed". During EPON registeration request, SDK sets it to the contetns of Coprocessor 0 Count as a pseudo‑random number|
