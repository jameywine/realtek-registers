---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: HSB_CTRL

## Details

*Name* HSB_CTRL

*Offset* 0x28000

*Feature* [PARSER_HSB](../../feature/PARSER_HSB)

*Bit Offset:* 64

## Description

Control register to access HSB data

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|63:40|RESERVED||
|39:32|LATCH_HSA_REASON||
|31|VALID|x1 indicates send HSBDATA0 HSBDATA18 to ALE|
|30:28|RESERVED||
|27|LATCH_IGR_PBO|latched Egress packet buffer overflow?|
|26:16|LATCH_EGR_PMSK|latched Egress port mask?|
|15:5|LATCH_IGR_PMSK|latched Igress port mask? |
|4:2|LATCH_MODE|HSB_DATA latched method<br>0x0: all latch<br>0x1: non-latch<br>0x2: latch first Drop<br>0x3: latch first Pass<br>0x4: latch first trap to CPU<br>0x5: latch drop pkt<br>0x6: latch trap to CPU<br>0x7: latch for ACL action|
|1:0|RESERVED||
