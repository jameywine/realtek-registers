---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: DOT3_EPON_FEC_UNCORRECTED_BLOCKS

## Details

*Name* DOT3_EPON_FEC_UNCORRECTED_BLOCKS

*Offset* 0x32E88

*Feature* [STATISTIC_COUNTERS](../../feature/STATISTIC_COUNTERS)

## Description

dot3EponFecUncorrectableBlocks

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:0|DOT3EPONFECUNCORRECTABLEBLOCKS|For 10PASS-TS, 2BASE-TL, and 1000BASE-PX PHYs, it is a count of uncorrectable FEC blocks. This counter will not increment for other PHY Types. Increment the counter by one for each FEC block that is determined to be uncorrectable by the FEC function in the PHY.|
