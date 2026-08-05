---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GTC_DS_ALLOC_IND

## Details

*Name* GPON_GTC_DS_ALLOC_IND

*Offset* 0x7010C0

*Feature* [GTC_DOWNSTREAM](../../feature/GTC_DOWNSTREAM)

## Description

AllocID operation indication

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31:16|RESERVED||
|15|ALLOCID_OP_REQ|CPU write 0x0 then 0x1 to start an operation.|
|14|ALLOCID_OP_COMPL|Operation complete flag.<br>0x1: Operation complete.|
|13|ALLOCID_OP_HIT|0x0: ALLOCID_OP_RDATA is not valid since no item configured for this index.<br>0x1: ALLOCID_OP_RDATA is valid.|
|12:10|RESERVED||
|9:8|ALLOCID_OP_MODE|Operation code:<br>0b00: no operation<br>0b01: write operation<br>0b10: read operation<br>0b11: clean operation|
|7:5|RESERVED||
|4:0|ALLOCID_OP_IDX|Index of T-CONT of AllocID configuration.<br>AllocID filtering is done by CAM structure which is configured by software. ALLOCID_OP_xxx registers are provisioned for AllocID CAM configuration and enquiry. Operation should follow the procedure:<br>1. Write ALLOCID_OP_IDX and ALLOCID_OP_MODE.<br>2. Write ALLOCID_OP_WDATA if the operation is writing.<br>3. Write ’0’ then ’1’ to ALLOCID_OP_REQ<br>4. Wait until ALLOCID_OP_COMPL = ’1’<br>5. If the operation is reading, read ALLOCID_OP_HIT. If it’s high, go to 6; else there is no match for this index.<br>6. Read ALLOCID_OP_RDATA.|
