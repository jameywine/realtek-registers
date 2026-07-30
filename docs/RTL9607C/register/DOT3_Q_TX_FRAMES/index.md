---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: DOT3_Q_TX_FRAMES

## Details

*Name* DOT3_Q_TX_FRAMES

*Offset* 0x32D80

*Feature* [STATISTIC_COUNTERS](../../feature/STATISTIC_COUNTERS)

*Bit Offset:* 32

*Array Range:* 0-63

## Description

dot3ExtPkgStatTxFramesQueue

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:0|DOT3EXTPKGSTATTXFRAMESQUEUE|A count of the number of times a frame transmisRO sion occurs from the corresponding ’Queue’. Increment the counter by one for each frame transmitted, which is an output of the ’Queue’.|
