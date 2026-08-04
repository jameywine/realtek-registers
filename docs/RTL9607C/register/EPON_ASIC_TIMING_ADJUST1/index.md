---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: EPON_ASIC_TIMING_ADJUST1

## Details

*Name* EPON_ASIC_TIMING_ADJUST1

*Offset* 0x36004

*Feature* [EPON_CONFIGURATION](../../feature/EPON_CONFIGURATION)

## Description

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:24|CFG_EP_IPG||
|23:16|RPT_TMG|control timing to get Queue information<br>8’d0: report pkt end at grant end<br>8’d1: ahead 1T (1T = 8ns)<br>8’d2: ahead 2T<br>8’d3: ahead 3T<br>...|
|15:8|REG_TMG|control timing to get send regsiter pkt<br>8’d0: report pkt begin after random delay<br>8’d1: ahead 1T<br>8’d2: ahead 2T<br>8’d3: ahead 3T<br>...|
|7:0|QU_TMG|control timing to get Queue information<br>8’d0: at begening of the grant<br>8’d1: ahead 1T<br>8’d2: ahead 2T<br>8’d3: ahead 3T<br>...|
