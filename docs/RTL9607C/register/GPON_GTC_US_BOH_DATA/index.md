---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GTC_US_BOH_DATA

## Details

*Name* GPON_GTC_US_BOH_DATA

*Offset* 0x705080

*Feature* [GTC_UPSTREAM](../../feature/GTC_UPSTREAM)

*Bit Offset:* 32

*Array Range:* 0-11

## Description

Upsteam Burst Overhead data

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:8|RESERVED||
|7:0|BOH_DATA|Burst Overhead Data.<br>BOH_DATA: total 12 bytes and the content are as below.<br>Guard bits: A bytes<br>Type 1 preamble: B bytes<br>Type 2 preamble: C bytes<br>Type 3 preamble: D bytes<br>Delimiter: 3 bytes<br><br>BOH_LEN: total burst overhead length<br>BOH_REP: indicate the byte of the type 3 preamble which will be repeated. BOH_REP should indicate to the location of (A+B+C).<br>If the BOH_LEN <= 12, the GPON MAC will send the first BOH_LEN bytes in BOH_DATA.<br>If the BOH_LEN > 12, the GPON MAC will send first (BOH_REP) bytes, and repeat the byte indicated by BOH_REP until the transmit bytes reach to (BOH_LEH - 3), and then send last 3 bytes of BOH_DATA (Delimiter).|
