---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: STAT_PORT_RX_MIB

## Details

*Name* STAT_PORT_RX_MIB

*Offset* 0x32600

*Feature* [STATISTIC_COUNTERS](../../feature/STATISTIC_COUNTERS)

*Bit Offset:* 1024

*Port Range:* 0-11

## Description

Per port stanadard RX MIB counters.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|1023:992|IFINOCTETS_L|ifInOctets:<br>32 bits counter. The total number of octets received on the interface, including framing characters.<br>ifHCInOctets:<br>64 bits counter. Same as ifInOctets.<br>Note: count with tag length|
|991:960|IFINOCTETS_H|ifInOctets:<br>32 bits counter. The total number of octets received on the interface, including framing characters.<br>ifHCInOctets:<br>64 bits counter. Same as ifInOctets.<br>Note: count with tag length|
|959:928|ETHERSTATSCRCALIGNERRORS|The total number of packets received that had a length (excluding framing bits, but including FCS octets) of between 64 and 1518 octets, inclusive, but had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non-integral number of octets (Alignment Error).<br>Note: count w/wo tag length depends on RX_CNT_TAG|
|927:896|DOT3STATSSYMBOLERRORS|For an interface operating at 100 Mb/s, the number of times there was an invalid data symbol when a valid carrier was present.|
|895:864|DOT3INPAUSEFRAMES|A count of MAC Control frames received on this interface with an opcode indicating the PAUSE operation.|
|863:832|DOT3CONTROLINUNKNOWNOPCODES|A count of MAC Control frames received on this interface that contain an opcode that is not supported by this device.<br>Note: ether type = 8808 and opcode != 0001 in non-PON/0001 to 0006 in PON|
|831:800|ETHERSTATSFRAGMENTS|The total number of packets received that were less than 64 octets in length (excluding framing bits but including FCS octets) and had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non-integral number of octets (Alignment Error)<br>Note: count w/wo tag length depends on RX_CNT_TAG|
|799:768|ETHERSTATSJABBERS|The total number of packets received that were longer than 1518 octets (excluding framing bits, but including FCS octets), and had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non-integral number of octets (Alignment Error).<br>Note: count w/wo tag length depends on RX_CNT_TAG|
|767:736|IFINUCASTPKTS|The number of packets, delivered by this sub-layer to a higher (sub-)layer, which were not addressed to a multicast or broadcast address at this sub-layer.<br>Note: only count valid frame.|
|735:704|ETHERSTATSDROPEVENTS|The total number of events in which packets were dropped by the probe due to lack of resources. Note that this number is not necessarily the number of packets dropped; it is just the number of times this condition has been detected.<br>Note: drop before ALE due to lack of resources, ex. no system packet buffer, receiving packets after sending pause ON frame.|
|703:672|IFINMULTICASTPKTS|The number of packets, delivered by this sub-layer to a higher (sub-)layer, which were addressed to a multicast address at this sub-layer (Number of received valid multicast packets).<br>Note: only count valid frame.|
|671:640|IFINBROADCASTPKTS|The number of packets, delivered by this sub-layer to a higher (sub-)layer, which were addressed to a broadcast address at this sub-layer (Number of received valid broadcast packets).<br>Note: only count valid frame.|
|639:608|RX_ETHERSTATSPKTS1519TOMAXOCTETS|The total number of packets (including bad packets) received that were between 1519 and Max octets in length inclusive (excluding framing bits but including FCS octets).<br>Note: count w/wo tag length depends on RX_CNT_TAG|
|607:576|RESERVED||
|575:544|RX_ETHERSTATSUNDERSIZEPKTS|The total number of packets received that were less than 64 octets long (excluding framing bits, but including FCS octets) and were otherwise well formed. Note: count w/wo tag length depends on RX_CNT_TAG<br>Note: under size including drop or forward|
|543:512|RX_ETHERSTATSOVERSIZEPKTS|The total number of packets received that were longer than 1518 octets (excluding framing bits, but including FCS octets) and were otherwise well formed.<br>Note: count w/wo tag length depends on RX_CNT_TAG|
|511:480|RX_ETHERSTATSPKTS64OCTETS|The total number of packets (including bad packets) received that were 64 octets in length (excluding framing bits but including FCS octets).<br>Note: count w/wo tag length depends on RX_CNT_TAG|
|479:448|RX_ETHERSTATSPKTS65TO127OCTETS|The total number of packets (including bad packets) received that were between 65 and 127 octets in length inclusive (excluding framing bits but including FCS octets).<br>Note: count w/wo tag length depends on RX_CNT_TAG|
|447:416|RX_ETHERSTATSPKTS128TO255OCTETS|The total number of packets (including bad packets) received that were between 128 and 255 octets in length inclusive (excluding framing bits but including FCS octets).<br>Note: count w/wo tag length depends on RX_CNT_TAG|
|415:384|RX_ETHERSTATSPKTS256TO511OCTETS|The total number of packets (including bad packets) received that were between 256 and 511 octets in length inclusive (excluding framing bits but including FCS octets).<br>Note: count w/wo tag length depends on RX_CNT_TAG|
|383:352|RX_ETHERSTATSPKTS512TO1023OCTETS|The total number of packets (including bad packets) received that were between 512 and 1023 octets in length inclusive (excluding framing bits but including FCS octets).<br>Note: count w/wo tag length depends on RX_CNT_TAG|
|351:320|RX_ETHERSTATSPKTS1024TO1518OCTETS|The total number of packets (including bad packets) received that were between 1024 and 1518 octets in length inclusive (excluding framing bits but including FCS octets).<br>Note: count w/wo tag length depends on RX_CNT_TAG|
|319:0|RESERVED||
