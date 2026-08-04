---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: DOS_CFG

## Details

*Name* DOS_CFG

*Offset* 0x26004

*Feature* [DENIAL_OF_SERVICE_ATTACK_PREVENTION](../../feature/DENIAL_OF_SERVICE_ATTACK_PREVENTION)

## Description

DOS function configuration register

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31|DOS_ICMPFLOOD_ACT|0b0:Drop while ICMP packets number is over threshold<br>0b1:Trap ICMP packets|
|30|DOS_FINFLOOD_ACT|0b0:Drop while TCP FIN packets number is over threshold<br>0b1:Trap TCP FIN packets|
|29|DOS_SYNFLOOD_ACT|0b0:Drop while TCP SYN packets number is over threshold<br>0b1:Trap TCP SYN packets|
|28|DOS_SYNWITHDATA_ACT|Treating type for packets match DOS_SYNWITHDATA<br>0b0:Drop<br>0b1:Trap|
|27|DOS_UDPBOMB_ACT|Treating type for packets match DOS_UDPBOMB<br>0b0:Drop<br>0b1:Trap|
|26|DOS_PINGOFDEATH_ACT|Treating type for packets match DOS_PINGOFDEATH<br>0b0:Drop<br>0b1:Trap|
|25|DOS_ICMPFRAGMENT_ACT|Treating type for packets match DOS_ICMPFRAGMENT<br>0b0:Drop<br>0b1:Trap|
|24|DOS_TCPFRAGERROR_ACT|Treating type for packets match DOS_TCPFRAGERROR<br>0b0:Drop<br>0b1:Trap|
|23|DOS_TCPSHORTHDR_ACT|Treating type for packets match DOS_TCPSHORTHDR<br>0b0:Drop<br>0b1:Trap|
|22|DOS_SYN1024_ACT|Treating type for packets match DOS_SYN1024<br>0b0:Drop<br>0b1:Trap|
|21|DOS_NULLSCAN_ACT|Treating type for packets match DOS_NULLSCAN<br>0b0:Drop<br>0b1:Trap|
|20|DOS_XMASCAN_ACT|Treating type for packets match DOS_XMASCAN<br>0b0:Drop<br>0b1:Trap|
|19|DOS_SYNFINSCAN_ACT|Treating type for packets match DOS_SYNFINSCAN<br>0b0:Drop<br>0b1:Trap|
|18|DOS_BLATATTACKS_ACT|Treating type for packets match DOS_BLATATTACKS<br>0b0:Drop<br>0b1:Trap|
|17|DOS_LANDATTACKS_ACT|Treating type for packets match DOS_LANDATTACKS<br>0b0:Drop<br>0b1:Trap|
|16|DOS_DAEQSA_ACT|Treating type for packets match DOS_DAEQSA<br>0b0:Drop<br>0b1:Trap|
|15|DOS_ICMPFLOOD|Receiving ICMP packet number is over threshold, unit per 1ms|
|14|DOS_FINFLOOD|Receiving TCP FIN packet number is over threshold, unit per 1ms|
|13|DOS_SYNFLOOD|Receiving TCP SYN packet number is over threshold, unit per 1ms|
|12|DOS_SYNWITHDATA|1.IP length > IP header + TCP header length while SYN flag is set 1<br>2. IP More Fragment and Offset > 0 while SYN is set to 1|
|11|DOS_UDPBOMB|UDP length > IP payload length|
|10|DOS_PINGOFDEATH|IP packet size > 65535 bytes, ((IP offset *8) + (IP length) (IPIHL *4))>65535|
|9|DOS_ICMPFRAGMENT|ICMPv4/ICMPv6 data unit carried in a fragmented IP datagram|
|8|DOS_TCPFRAGERROR|the Frangment_Offset=1 in anyfragment of a fragmented IP datagram carrying part of TCP data|
|7|DOS_TCPSHORTHDR|the length of a TCP header carried in an unfragmented IP(IPv4 and IPv6) datagram or the first fragment of a fragmented IP(IPv4) datagram is less than MIN_TCP_Header_Size(20 bytes)|
|6|DOS_SYN1024|TCP SYN packets with source port less than 1024|
|5|DOS_NULLSCAN|TCP packets while sequence number is zero and all contorl bits are zeros.|
|4|DOS_XMASCAN|TCP packets while sequence number is zero and FIN,URG,PSH bits are set|
|3|DOS_SYNFINSCAN|TCP packets while SYN and FIN bits are set|
|2|DOS_BLATATTACKS|packets while the TCP/UDP SPORT is the same as DPORT destination TCP/UDP port|
|1|DOS_LANDATTACKS|packets while SIP is the same as DIP(support IPv4 only)|
|0|DOS_DAEQSA|packets while SMAC is the same as DMAC|
