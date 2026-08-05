---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GEM_US_INTR_STS

## Details

*Name* GPON_GEM_US_INTR_STS

*Offset* 0x706008

*Feature* [GEM_UPSTREAM](../../feature/GEM_UPSTREAM)

## Description

GEM upstream intrrupt status

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:10|RESERVED||
|9|SD_VALID_LONG_IND|0x1: Indicate the Signal Detect valid more than 125 us.|
|8|SD_DIFF_HUGE_IND|0x1: Indicate the Signal Detect and the TX Burst enable has the huge difference for the Transmit Optical Module. It depend on the parameter SD_DIFF_CYCYES.|
|7|REQUEST_DELAY_IND|0x1: Indicate the GTC_US need request the next 125us packets but the Switch also is busy on the last 125us request-acknowledge.|
|6|BC_LESS6_IND|0x1: Indicate the Byte Counter don’t take less than 6 and as Empty TCONT by Switch.|
|5|ERR_PLI_IND|0x1: Indicate the PLI mismatching with the input cycle from the Switch.|
|4|BURST_TM_LARGER_GTC_IND|0x1: Indicate the TM (Switch) has the larger burst bytes than the GTC indication. In this case, GEM module will insert IDLE until bank (125us) end.|
|3|BANK_TOO_INDUCH_AT_END_IND|0x1: Indicate the 1k bytes Bank has too much data at the time of leave 800 cycles (bytes). It will force the signal buffer full indication to un-valid in order to let the Switch can send the next bank data. It means the Switch gives too many traffic from|
|2|BANK_REMAIN_AFRD_IND|0x1: Indicate the Bank has the remained data after 125us bank read.<br>It means the Switch give too many traffic from request. (Too many response times or too many bytes in one response, etc.).|
|1|BANK_OVERFL_IND|0x1: Indicate Bank overflow.<br>It means the Switch doesn’t have the true back press machine.|
|0|BANK_UNDERFL_IND|0x1: Indicate Bank underflow.<br>It is as timeout of request to response of interface. Insert IDLE in this case.|
