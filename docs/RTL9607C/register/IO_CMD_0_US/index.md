---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: IO_CMD_0_US

## Details

*Name* IO_CMD_0_US

*Offset* 0xF05434

*Feature* [CPU_IF](../../feature/CPU_IF)

## Description

PON Upstream IO Command Register.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31|MAX_DMA_SEL_0|Select the dma burst size on bus(memory controller should assert continuous btrdy).<br>00:16 DW(1DW=4B)<br>01:32 DW<br>10:64 DW|
|30|RESERVED||
|29|MAX_DMA_SEL_1||
|28|EARLY_TX_EN|0: disable, 1: enable. Disable early tx by GAMC while tx command descriptor.IPCS, UDPCS or TCPCS are set to high|
|27:21|RESERVED||
|20:19|TX_FIFO_THR|Tx Threshold: Specifies the threshold level in the Tx FIFO to begin the transmission. When the byte count of the data in the Tx FIFO reaches this level, (or the FIFO contains at least one complete packet or the end of a packet) the Ethernet module will transmit this packet.<br>00:128B.<br>01:256B.<br>10:512B.<br>11:1024B.|
|18:17|DUMMY_0_US||
|16:13|RESERVED||
|12:11|RX_FIFO_THR|Rx Threshold: Specifies the threshold level in the Rx FIFO to begin the transmission. When the byte count of the data in the Rx FIFO reaches this level, (or the FIFO contains at least one complete packet or the end of a packet) the Ethernet module will transmit this packet.<br>00 256 bytes<br>10 64 bytes<br>11 128 bytes|
|10:8|RESERVED||
|7:6|RX_MAX_DMA_SEL|Set to 0x1 by SDK during PBO init|
|5|GMII_RX_EN|MII Rx Enable|
|4|GMII_TX_EN|MII Tx Enable|
|3:0|RESERVED||
