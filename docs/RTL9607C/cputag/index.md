---
tags:
  - RTL9607C
  - CPU Tags
---

# RTL9607C CPU tags

## Frame direction:  RX

|Name|LSB|Bits|Description|
| :--- | :--- | :--- | :--- |
|own|0|1|Indicates that descriptor is owned by NIC|
|eor|1|1|Indicates the end of descriptor ring|
|fs|2|1|Indicates the first segment of a packet|
|ls|3|1|Indicates the final segment of a packet|
|crcerr|4|1|Indicates the CRC error|
|ipv4csf|5|1|Indicates L3 checksum failure in IPv4 packet|
|l4csf|6|1|Indicates UDP/TCP/ICMP/IGMP checksum failure in IPv4/IPv6 packet|
|rcdf|7|1|Indicates Rx close DMA Failure|
|ipfrag|8|1|Indicates this is IP fragment packet|
|pppoetag|9|1|Indicates the precense of PPPoE Tag|
|rwt|10|1|Indicates that the recieved packet length exceeds 1536(0x600) bytes, and stop recieve engine|
|rsvd1|11|7||
|data_length|18|14|Indicates the number of bytes of data on the page pointed by the descriptor|
|cputag|32|1|Indicates that the recieved packet is cputag packet|
|ptp_in_cpu_tag_exist|33|1|Indicates the existance of Ethernet AV info in CPU tag header|
|svlan_tag_exist|34|1|Indicates if the SVLAN header exist|
|reason|35|8|Indicates the trap reason|
|rsvd_1|43|4||
|ctagva|47|1|Indicates the recieved packet is an IEEE802.1Q VLAN Tag (0x8100) available packet|
|cvlan_tag|48|16|Indicates the Vlan Tag value when ctagva is set |
|internal_priority|64|3|Indicates the internal priority for RX ring mapping|
|pon_sid_or_extspa|67|7|Indicates whether this field is pon_stream_id, when cputag.spa set to spa_pon, or extspa when cputag.spa set to spa_cpu |
|l3routing|74|1|Indicates the frame is "intended routed frames"|
|origformat|75|1|Indicates the the recieved frame by NIC is the original packet's fortmat before switch loopkup|
|src_port_num|76|4|Indicates the recieve source port number|
|fbi|80|1||
|fb_hash_or_dst_portmsk|81|15|Indicates whether it is flow-based hash index, if reason is FB, or destination port mask otherwise|

## Frame direction:  TX

|Name|LSB|Bits|Description|
| :--- | :--- | :--- | :--- |
|own|0|1|Descriptor is owned by NIC|
|eor|1|1|End of descriptor ring|
|fs|2|1|Tx First segment of a packet|
|ls|3|1|Tx Final segment of a packet|
|ipcs|4|1|Calculate IP checksum|
|l4cs|5|1|Calculate UDP/TCP/ICMP/IGMP checksum|
|tpid_sel|6|1|Select tpid which used to insert / remark S-tag|
|stag_aware|7|1|Aware S-tag or not|
|crc|8|1|If this bit is set then append CRC at the end of Ethernet frame. For shorter frames (<64KB), this bit must be set to 1|
|rsvd|9|6||
|data_length|15|17|Tx buffer packet size|
|cputag|32|1|Force CPU NIC to generate Realtek CPU-tag. Always set to 1|
|tx_svlan_action|33|2|CPU NIC VLAN tx action. SVLAN action for this egress frame 0: inact, 1: insert SVLAN header, 2: remove SVLAN header, 3: remarking SVID|
|tx_cvlan_action|35|2|CPU NIC CVLAN tx action. CVLAN action for this egress frame 0: inact, 1: insert CVLAN header, 2: remove CVLAN header, 3: remarking CVID|
|tx_portmask|37|11|Command siwtch force forwarding using this tx port mask|
|cvlan_vidl|48|8|CVLAN tag vid[7:0]|
|cvlan_prio|56|3|CVLAN tag priority|
|cvlan_cfi|59|1|CVLAN tag CFI|
|cvlan_vidh|60|4|CVLAN tag vid[11:8]|
|rsvd1|64|4||
|aspri|68|1|Turn on CPU force priority for this packet|
|cputag_pri|69|3|CPU force priority (for switch internal priority). This field is valid when aspri is set to 1|
|keep|72|1|Command switch to keep original packet and not modify packet (remarking, VLAN translation ...)|
|rsvd2|73|1||
|dislrn|74|1|Command switch to disable switch l2 learning for this packet|
|cputag_psel|75|1|For PON stream id (for GPON)/LLID index (for EPON) selections. This bit is valid when tx_portmask includes PON port.|
|gmac_id|76|2|ID of GMAC?|
|l34_keep|78|1| Similar to keep but for l34?|
|rsvd3|79|1||
|extspa|80|3|Source  extension port|
|tx_pppoe_action|83|2|Egress action for PPPoE header whose Ether Type = 0x8864|
|tx_pppoe_idx|85|4|PPPoE index pointed to an entry of the pppoe table in switch. Switch TX-MAC look PPPoE table up by this index to get PPPoE session ID|
|tx_dst_stream_id|89|7|if cputag_psel is set, it is PON Stream id/LLID index, and if ptp is set, it is PON Queue id|
|lgsen|96|1|Large Send offload enable|
|lgmtu|97|11|Large send max transmit unit value|
|rsvd|108|4||
|svlan_vidl|112|8|SVLAN tag vid[7:0] |
|svlan_prio|120|3|SVLAN tag priority|
|svlan_cfi|123|1|SVLAN tag CFI|
|svlan_vidh|124|4|SVLAN tag vid[11:8]|
