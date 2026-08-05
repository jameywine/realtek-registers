---
tags:
  - RTL9607C
  - Register
  - Register Fields
---

# RTL9607C register: GPON_GEM_US_PTI_CFG

## Details

*Name* GPON_GEM_US_PTI_CFG

*Offset* 0x706020

*Feature* [GEM_UPSTREAM](../../feature/GEM_UPSTREAM)

## Description

GEM upstream PTI configuration

## Fields


|Bit(s)|Field Name|Description|
| :--- | :--- | :--- |
|31|FS_GEM_IDLE|0x1: Forceto send the IDLE only and don’t care the data from the Switch. It is just for test.|
|30:15|RESERVED||
|14:12|PTI_VECTOR3|Translate the input token (OMCI,ENDFRAG) to PTI:<br>(1,1): PTI_VECTOR3.<br>It means OMCI type with End fragment.|
|11|RESERVED||
|10:8|PTI_VECTOR2|Translate the input token (OMCI,ENDFRAG) to PTI:<br>(1,0): PTI_VECTOR2.<br>It means OMCI type with End fragment.|
|7|RESERVED||
|6:4|PTI_VECTOR1|Translate the input token (OMCI,ENDFRAG) to PTI:<br>(0,1): PTI_VECTOR1.<br>It means OMCI type with End fragment.|
|3|RESERVED||
|2:0|PTI_VECTOR0|Translate the input token (OMCI,ENDFRAG) to PTI:<br>(0,0): PTI_VECTOR0.<br>It means OMCI type with End fragment.|
