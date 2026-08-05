---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GTC_DS_PORT_IND

## Details

*Name* GPON_GTC_DS_PORT_IND

*Offset* 0x701100

*Feature* [GTC_DOWNSTREAM](../../feature/GTC_DOWNSTREAM)

## Description

GEM Port ID operation indication

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15|PORTID_OP_REQ|CPU write 0x0 then 0x1 to start an operation.|
|14|PORTID_OP_COMPL|Operation complete flag.<br>0x1: Operation complete.|
|13|PORTID_OP_HIT|0x0: PORTID_OP_RDATA is not valid since no item configured for this index.<br>0x1: PORTID_OP_RDATA is valid.|
|12:10|RESERVED||
|9:8|PORTID_OP_MODE|Operation code:<br>0b00: no operation<br>0b01: write operation<br>0b10: read operation<br>0b11: clean operation|
|7|RESERVED||
|6:0|PORTID_OP_IDX|GEM Port index.<br>PortID filtering is done by CAM structure which is configured by software. PORTID_OP_xxx registers are provisioned for PortID CAM configuration and enquiry. Operation should follow the procedure:<br>1. Write PORTID_OP_IDX and PORTCID_OP_MODE<br>2. Write PORTID_OP_WDATA if the operation is writing.<br>3. Write ’0’ then ’1’ to PORTID_OP_REQ<br>4. Wait until PORTID_OP_COMPL = ’1’<br>5. If the operation is reading, read PORTID_OP_HIT. If it’s high, go to 6; else there is no match for this index.<br>6. Read PORTID_OP_RDATA.|
