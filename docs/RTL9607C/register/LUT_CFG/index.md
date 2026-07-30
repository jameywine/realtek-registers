---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: LUT_CFG

## Details

*Name* LUT_CFG

*Offset* 0x17000

*Feature* [ADDRESS_TABLE_LOOKUP](../../feature/ADDRESS_TABLE_LOOKUP)

## Description

LUT global control register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:30|LUT_IPMC_VLAN_MODE|lookup VLAN mode of layer2 ip multicast switching.<br>0: IVL_SVL VLAN mode.<br>1: Force no VLAN mode.<br>2: Force VLAN mode.|
|29|L34_L2_LOOKUP_MISS_ACT||
|28:27|LUT_L2UC_ACT|unicast forwarding action when destination address lookup hit.<br>0: lut.<br>1: fb.<br>2: fb-lut.|
|26|LUT_ENTRY_FULL_ACT|action when over learning the same hash result entry.<br>0: forward.<br>1: to CPU.|
|25|LUT_L34_ARP_USAGE_AS_KNOWN||
|24:23|LUT_IPMC_HASH|Hash algorithm for incoming IP multicast packet to lookup forwarding decision<br>0b00:using {DMAC,FID} hash algorithm<br>0b01:using {DIP,SIP} hash algorithm<br>0b10:hash method {GIP, VID}|
|22|LINKDOWN_AGEOUT|Link down port aging out setting<br>0b0:disable aging out<br>0b1:enable force aging out all L2 lookup entries belong to link down ports|
|21|BCAM_DIS|Binary CAM usage setting<br>0b0:enable<br>0b1:disable|
|20:0|AGE_SPD|L2 lookup table aging speed/period for each 2K entries, unit 0.1 sec|
