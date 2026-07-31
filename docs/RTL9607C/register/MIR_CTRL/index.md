---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: MIR_CTRL

## Details

*Name* MIR_CTRL

*Offset* 0x1C21C

*Feature* [MIRRORING](../../feature/MIRRORING)

## Description

Mirror control register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:27|RESERVED||
|26:16|MIR_SRC_PMSK|Mirror Source Port Mask|
|15:7|RESERVED||
|6|MIR_ISO|Enable the traffic isolation on monitor port.<br>0b0 Normal operation.<br>0b1 The monitor port will accept only the packets from the source port.|
|5|MIR_TX|Enable the mirror function on TX of the source port.<br>0b0 Disable.<br>0b1 Enable.|
|4|MIR_RX|Enable the mirror function on RX of the source port.<br>0b0 Disable.<br>0b1 Enable.|
|3:0|MIR_MONITOR_PORT|Select the monitor port to be mirroring|
