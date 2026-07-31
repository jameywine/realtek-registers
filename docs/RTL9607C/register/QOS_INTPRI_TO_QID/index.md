---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: QOS_INTPRI_TO_QID

## Details

*Name* QOS_INTPRI_TO_QID

*Offset* 0x1C290

*Feature* [QUEUE_MANAGEMENT](../../feature/QUEUE_MANAGEMENT)

*Bit Offset:* 3

*Array Range:* 0-7

*Port Range:* 0-3

## Description

Specify valid queue ID to each internal-priority in different QID mapping table of output queue.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|2:0|PRI_TO_QID|Internal priority mapping to queue ID<br>0x0 0x7: queue ID 0 7|
