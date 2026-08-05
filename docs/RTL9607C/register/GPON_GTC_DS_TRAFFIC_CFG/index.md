---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GTC_DS_TRAFFIC_CFG

## Details

*Name* GPON_GTC_DS_TRAFFIC_CFG

*Offset* 0x701400

*Feature* [GTC_DOWNSTREAM](../../feature/GTC_DOWNSTREAM)

*Bit Offset:* 32

*Array Range:* 0-127

## Description

Traffic type configuraiton for downstream GEM ports.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:5|RESERVED||
|4:0|TRAFFIC_TYPE_CFG|Traffic Type configuration for downstream GEM ports.<br>Bit 4: AES encryption/decryption is enabled on this GEM port<br>Bit 3: Reserved<br>Bit 2: This GEM port is for OMCI<br>Bit 1: This GEM port is for Ethernet service<br>Bit 0: Only valid when bit 1 is set to 1, this GEM port is for multicast Ethernet service, GPON MAC will apply multicast filtering on received packets.|
