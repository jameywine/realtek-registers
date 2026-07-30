---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: STAT_PORT_TX_MIB

## Details

*Name* STAT_PORT_TX_MIB

*Offset* 0x32000

*Feature* [STATISTIC_COUNTERS](../../feature/STATISTIC_COUNTERS)

*Bit Offset:* 1024

*Port Range:* 0-11

## Description

Per port stanadard TX MIB counters.

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|1023:992|TX_ETHERSTATSMULTICASTPKTS|The total number of good packets received that were directed to a multicast address. Note that this number does not include packets directed to the broadcast address.|
|991:960|TX_ETHERSTATSBROADCASTPKTS|The total number of good packets received that were directed to the broadcast address. Note that this does not include multicast packets.|
|959:928|TX_ETHERSTATSUNDERSIZEPKTS|The total number of packets received that were less than 64 octets long (excluding framing bits, but including FCS octets) and were otherwise well formed.<br>Note: count w/wo tag length depends on TX_CNT_TAG|
|927:896|TX_ETHERSTATSOVERSIZEPKTS|The total number of packets received that were longer than 1518 octets (excluding framing bits, but including FCS octets) and were otherwise well formed.<br>Note: count w/wo tag length depends on RX_CNT_TAG|
|895:864|TX_ETHERSTATSPKTS64OCTETS|The total number of packets (including bad packets) received that were 64 octets in length (excluding framing bits but including FCS octets).<br>Note: count w/wo tag length depends on TX_CNT_TAG|
|863:832|TX_ETHERSTATSPKTS65TO127OCTETS|The total number of packets (including bad packets) received that were between 65 and 127 octets in length inclusive (excluding framing bits but including FCS octets).<br>Note: count w/wo tag length depends on TX_CNT_TAG|
|831:800|TX_ETHERSTATSPKTS128TO255OCTETS|The total number of packets (including bad packets) received that were between 128 and 255 octets in length inclusive (excluding framing bits but including FCS octets).<br>Note: count w/wo tag length depends on TX_CNT_TAG|
|799:768|TX_ETHERSTATSPKTS256TO511OCTETS|The total number of packets (including bad packets) received that were between 256 and 511 octets in length inclusive (excluding framing bits but including FCS octets).<br>Note: count w/wo tag length depends on TX_CNT_TAG|
|767:736|TX_ETHERSTATSPKTS512TO1023OCTETS|The total number of packets (including bad packets) received that were between 512 and 1023 octets in length inclusive (excluding framing bits but including FCS octets).<br>Note: count w/wo tag length depends on TX_CNT_TAG|
|735:704|TX_ETHERSTATSPKTS1024TO1518OCTETS|The total number of packets (including bad packets) received that were between 1024 and 1518 octets in length inclusive (excluding framing bits but including FCS octets).<br>Note: count w/wo tag length depends on TX_CNT_TAG|
|703:672|IFOUTOCTETS_L|ifOutOctets: 32 bits counter. The total number of octets transmitted out of the interface, including framing characters.<br>ifHCOutOctets: 64 bits counter. Same as ifOutOctets.<br>Note: count with tag length|
|671:640|IFOUTOCTETS_H|ifOutOctets: 32 bits counter. The total number of octets transmitted out of the interface, including framing characters.<br>ifHCOutOctets: 64 bits counter. Same as ifOutOctets.<br>Note: count with tag length|
|639:608|DOT3STATSSINGLECOLLISIONFRAMES|A count of frames that are involved in a single collision, and are subsequently transmitted successfully.|
|607:576|DOT3STATSMULTIPLECOLLISIONFRAMES|A count of frames that are involved in more than one collision and are subsequently transmitted successfully.|
|575:544|DOT3STATSDEFERREDTRANSMISSIONS|A count of frames for which the first transmission attempt on a particular interface is delayed because the medium is busy.<br>Note: in half-duplex mode. The the counter does not include frames involved in collisions.|
|543:512|DOT3STATSLATECOLLISIONS|The number of times that a collision is detected on a particular interface later than one slotTime into the transmission of a packet.|
|511:480|ETHERSTATSCOLLISIONS|The best estimate of the total number of collisions on this Ethernet segment|
|479:448|DOT3STATSEXCESSIVECOLLISIONS|A count of frames for which transmission on a particular interface fails due to excessive collisions.|
|447:416|DOT3OUTPAUSEFRAMES|A count of MAC Control frames transmitted on this interface with an opcode indicating the PAUSE operation.|
|415:384|IFOUTDISCARDS|The number of outbound packets which were chosen to be discarded even though no errors had been detected to prevent their being transmitted. One possible reason for discarding such a packet could be to free up buffer space.|
|383:352|TX_ETHERSTATSPKTS1519TOMAXOCTETS|The total number of packets (including bad packets) received that were between 1519 and Max octets in length inclusive (excluding framing bits but including FCS octets).<br>Note: count w/wo tag length depends on TX_CNT_TAG|
|351:320|RESERVED||
|319:288|DOT1DTPPORTINDISCARDS|Count of valid frames received which were discarded (i.e., filtered) by the Forwarding Process.<br>Note: drop in ALE|
|287:256|IFOUTUCASTPKTS|The total number of packets that higher-level protocols requested be transmitted, and which were not addressed to a multicast or broadcast address at this sub-layer, including those that were discarded or not sent.<br>Note: discarded or not sent packets are count in.|
|255:224|IFOUTMULTICASTPKTS|The total number of packets that higher-level protocols requested be transmitted, and which were addressed to a multicast address at this sub-layer, including those that were discarded or not sent.<br>Note: discarded or not sent packets are count in.|
|223:192|IFOUTBROADCASTPKTS|The total number of packets that higher-level protocols requested be transmitted, and which were addressed to a broadcast address at this sub-layer, including those that were discarded or not sent.<br>Note: discarded or not sent packets are count in.|
|191:0|RESERVED||
