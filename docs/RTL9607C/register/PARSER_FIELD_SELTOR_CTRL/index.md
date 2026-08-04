---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: PARSER_FIELD_SELTOR_CTRL

## Details

*Name* PARSER_FIELD_SELTOR_CTRL

*Offset* 0x2322C

*Feature* [PARSER](../../feature/PARSER)

*Bit Offset:* 32

*Array Range:* 0-7

## Description

ACL 16-bits user defined field selector configuration

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:11|RESERVED||
|10:3|OFFSET|Offset in bytes.|
|2:0|FMT|Field selector format. It defines the start address for 16-bit data.<br>0x0:ASIC default setting 0x1: Raw packet(Start after SFD begin with DA)<br>0x2: LLC packet(Start after SA begin with length 0000-05FF)<br>0x3: ARP packet (Start from ARP Ethernet II EtherType 0x0806)<br>0x4: IPv4 packet (Start from IPv4 header)<br>0x5: IPv6 packet (Start from IPv6 header)<br>0x6: IP payload(Start from IP payload also means start of layer 4 packet)<br>0x7: L4 payload (Start after TCP/UDP/ICMP header)|
