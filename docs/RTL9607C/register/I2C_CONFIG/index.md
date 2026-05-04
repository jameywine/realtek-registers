---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: I2C_CONFIG

## Details

*Name* I2C_CONFIG

*Offset* 0x23004

*Feature* [INTERFACE](../../feature/INTERFACE)

*Bit Offset:* 32

*Array Range:* 0-1

## Description

I2C master configuration register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31|RESERVED||
|30:27|SCK_I_DELAY||
|26|EXT_SCK_5MS||
|25:24|WAIT_SCK||
|23|SCK_IO_STY||
|22|SDA_IO_STY||
|21|DATA_TRANS_FMT||
|20:14|SLV_ADDR|i2c device ID|
|13:12|REG_ADDR_WIDTH|i2c addr width, 0 - 8bits address, 1 - 16bits address, 2 - 24 bits address, 3 - 32 bits address|
|11:10|DATA_WIDTH|i2c data width, 0 - 8bits data, 1 - 16bits data, 2 - 24 bits data, 3 - 32 bits data|
|9:0|CLK_DIV||
