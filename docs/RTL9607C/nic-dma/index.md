---
tags:
  - RTL9607C
  - CPU NIC
  - Register
  - Register Fields
  - SoC Register Space
---

# RTL9607C NIC Registers

This is an attempt to create an approximate register layout of CPU NIC in RTL9607C. Since they are located SoC registry space, exact bit fields are not avaible in the `rtk_rtl9607c_regField_list.c`, and so some findings need to be made from various sources in SDK, NIC driver and etc. Luckily the `apollo_regField_list.c` file seems to contain large portion of the bit fields. And so, together with `re8686_rtl9607c.h`,  the rough bit fields were constructed.

The offsets are based off of the 3 GMAC base addresses, `0x18012000`, `0x18014000`,`0x18016000` respectively. 

## NIC_ID_CRTL0

*Offset* 0x0

### Description

Ethernet ID 0 - 3

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:24 | IDR3 | Ethernet ID 3 |
| 23:16 | IDR2 | Ethernet ID 2 |
| 15:8 | IDR1 | Ethernet ID 1 |
| 7:0 | IDR0 | Ethernet ID 0 |

## NIC_ID_CRTL1

*Offset* 0x4

### Description

Ethernet ID 4 - 5

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:16 | RESERVED ||
| 15:8 | IDR5 | Ethernet ID 5 |
| 7:0 | IDR4 | Ethernet ID 4 |

## NIC_MC_CRTL

*Offset* 0x8

### Description

Multicast Address Register 0 - 3

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:24 | MAR3 | Multicast Register 3 |
| 23:16 | MAR2 | Multicast Register 2 |
| 15:8 | MAR1 | Multicast Register 1 |
| 7:0 | MAR0 | Multicast Register 0 |

## NIC_MC_CRTL1

*Offset* 0xc

### Description

Multicast Address Register 4 - 7

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:24 | MAR7 | Multicast Register 7 |
| 23:16 | MAR6 | Multicast Register 6 |
| 15:8 | MAR5 | Multicast Register 5 |
| 7:0 | MAR4 | Multicast Register 4 |

## NIC_MIB0

*Offset* 0x10

### Description

Looks similar to Dump Tally Counter Command in [RTL8111B Datasheet](https://github.com/plappermaul/realtek-doc/blob/main/datasheets/RTL8111B_RTL8168B_Registers_DataSheet_1.0.pdf) ?

This is TX OK and RX OK portion

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:16 | RX_OK_CNT | Counter of Rx Ok Packets |
| 15:0 | TX_OK_CNT | Counter of Rx Ok Packets |

## NIC_MIB1

*Offset* 0x14

### Description

This is Tx Error and RX Error portion

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:16 | RX_ERR_CNT | Counter of Rx errors |
| 15:0 | TX_ERR_CNT | Counter of Tx Errors |

## NIC_MIB2

*Offset* 0x18

### Description

This is FAE and Missed Packets portion

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:16 | FAE | Counter of Frame Alignment Error packets |
| 15:0 | MISS_PKT | Counter of missed packets |

## NIC_MIB3

*Offset* 0x1c

### Description

This is Tx 1 Collision and Tx Multiple Collisions portition

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:16 | TX_MUL_COL | Counter of Tx Ok packets with more than 1 collision |
| 15:0 | TX_1_COL | Counter of Tx Ok packets with only 1 collision |

## NIC_MIB4

*Offset* 0x20

### Description

This is RX Ok Broadcast Collision and Rx Ok Phy portion

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:16 | RX_OK_BC | Counter of Rx Ok packets with broadcast destination ID |
| 15:0 | RX_OK_PHY | Counter of Tx Ok packets with physical address matching destination ID |

## NIC_MIB5

*Offset* 0x24

### Description

This is Tx Abort and Rx Ok Multicast portion

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:16 | TX_ABORT | Counter of Tx abort packets |
| 15:0 | RX_OK_MC | Counter of Rx Ok packets with multicast destination ID |

## NIC_MIB6

*Offset* 0x28

### Description

This is Tx underrun portion

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:16 | RDU_MISS_PKT | Counter of missed packets and Rx Descriptor Unavailable? |
| 15:0 | TX_UNDER_RUN | Counter of Tx underrun and discard packets |

## NIC_STS // TRSR

*Offset* 0x34

### Description

Transmit/Recieve Status Register?

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:4 | RESERVED ||
| 3 | TX_UNDER ||
| 2:0 | RESERVED ||

## NIC_COM // CMD

*Offset* 0x38

### Description

This is a Control / Command register 

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:4 | RESERVED ||
| 3 | RX_JUMBO | Receive Jumbo Support Enable: 1: Enable. 0: Disable. |
| 2 | RX_VLAN | Receive VLAN De-tagging Enable: 1: Enable. 0: Disable.|
| 1 | RX_CHKSUM | Receive Checksum Offload Enable: 1: Enable. 0: Disable.|
| 0 | RST | Set this bit to 1 to force NIC into a software reset state. It self-clears it after reset is complete|

## NIC_INTR

*Offset* 0x3c

### Description

Interrupt Register. This have mixes of Mask and Status bits.

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31 | ISR_RDU6 | Rx Descriptor Unavailable for RING6: When set, indicates Rx descriptor is unavailable. |
| 30 | ISR_RDU5 | Rx Descriptor Unavailable for RING5: When set, indicates Rx descriptor is unavailable. |
| 29 | ISR_RDU4 | Rx Descriptor Unavailable for RING4: When set, indicates Rx descriptor is unavailable. |
| 28 | ISR_RDU3 | Rx Descriptor Unavailable for RING3: When set, indicates Rx descriptor is unavailable. |
| 27 | ISR_RDU2 | Rx Descriptor Unavailable for RING2: When set, indicates Rx descriptor is unavailable. |
| 26 | ISR_SW_INT | Software Interrupt pending: When set to 1 indicates a software interrupt was forced |
| 25 | ISR_TDU | Tx Descriptor Unavailable: When set, this bit indicates that the Tx descriptor is unavailable.|
| 24 | ISR_LINK_CHG | Link Change: This bit is set to 1 when link status is changed.|
| 23 | ISR_TER | Transmit (Tx) Error: This bit set to 1 indicates that a packet transmission was aborted, due to excessive collisions. |
| 22 | ISR_TOK_TI | Transmit Interrupt: Indicates that the DMA of the last descriptor of RxIntMitigation number of Tx packet has completed and the last descriptor has been closed. |
| 21 | ISR_RDU | Rx Descriptor Unavailable for RING1: When set, indicates Rx descriptor is unavailable. |
| 20 | ISR_RER_OVF | Receive (Rx) Overflow Error |
| 19 | RESERVED ||
| 18 | ISR_RER_RUNT | Receive (Rx) Runt Error |
| 17 | RESERVED ||
| 16 | ISR_ROK | Receive (Rx) OK: In normal mode, this bit set to 1 indicates the successful completion of a packet reception. |
| 15 | IMR_RDU6 | Rx Descriptor Unavailable Interrupt for RING6 1: Enable. 0: Disable. |
| 14 | IMR_RDU5 | Rx Descriptor Unavailable Interrupt for RING5 1: Enable. 0: Disable. |
| 13 | IMR_RDU4 | Rx Descriptor Unavailable Interrupt for RING4 1: Enable. 0: Disable. |
| 12 | IMR_RDU3 | Rx Descriptor Unavailable Interrupt for RING3 1: Enable. 0: Disable. |
| 11 | IMR_RDU2 | Rx Descriptor Unavailable Interrupt for RING2 1: Enable. 0: Disable. |
| 10 | IMR_SW_INT | Software Interrupt 1: Enable. 0: Disable. |
| 9 | IMR_TDU | Tx Descriptor Unavailable Interrupt 1: Enable. 0: Disable. |
| 8 | IMR_LINK_CHG | Link Change Interrupt 1: Enable, 0: Disable. |
| 7 | IMR_TER | Transmit (Tx) Error Enable: 1: Enable. 0: Disable. |
| 6 | IMR_TOK_TI | Transmit Interrupt: Indicates that the DMA of the last descriptor of RxIntMitigation number of Tx packet has completed and the last descriptor has been closed. |
| 5 | IMR_RDU | Rx Descriptor Unavailable Interrupt for RING1 1: Enable. 0: Disable.|
| 4 | IMR_RER_OVF | Rx Error Overflow Interrupt 1: Enable, 0: Disable.|
| 3 | RESERVED ||
| 2 | IMR_RER_RUNT | Rx Error Runt Interrupt 1: Enable, 0: Disable. |
| 1 | RESERVED ||
| 0 | IMR_ROK | Rx OK Interrupt. 1: Enable, 0: Disable.|

## NIC_TC

*Offset* 0x40

### Description

Transmit Configuration Register

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:16 | RESERVED ||
| 15 | TX_JUMBO | This is set when enabling Tx Jumbo and cleared when disabling it|
| 12:10 | IFG2_0 | InterFrame Gap 2 |
| 9:8 | LBK1_0 | Digital Loopback test 00 : Normal operation, 11 : Loopback mode|
| 7:1 | RESERVED ||
| 0 | GMAC_PADDING | GMAC Padding 0: Enable, 1: Disable |

## NIC_RC

*Offset* 0x44

### Description

Recieve Configuration Register

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:8 | RESERVED ||
| 7 | HOME_PNA | HomePNA mode: When set to 1, will use crs pin doing tx deferring |
| 6 | AFLOW | Accept flow control : When set to 1, flow control packet will also be received & DMA to rx buffer for debug. Default is 0 |
| 5 | AER | Accept packets with CRC errors |
| 4 | AR | Accept Runt: This bit set to 1 allows the receiver to accept packets that are smaller than 64 bytes|
| 3 | AB | Accept Broadcast Packets: 1: Accept, 0: Reject |
| 2 | AM | Accept Multicast Packets: 1: Accept, 0: Reject|
| 1 | APM | Accept Physical Match Packets: 1: Accept, 0: Reject|
| 0 | AAP | Accept All Packets with Destination Address: 1: Accept, 0: Reject|

## NIC_CPUTAG

*Offset* 0x48

### Description

The CPUTAG Control Register

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31 | CTEN_RX | Enable parsing ingress packet with cputag format. |
| 27:24 | CT_TSIZE | Cputag size in egress pkt.<br>CTT_size:<br>4h0: 0 Byte<br>4h1: 4 Byte<br>4h2: 8Byte<br>4h3: 10Byte |
| 25:24 | CT_RSIZE_3_2 | |
| 24 | CT_DSLRN | In rtl8370s, Setting of Disable Learning field in tx cputag. Setting of Disable Learning field in RTL8368 or DSLRN field in RTL8307h tx cputag when short_dsc_format = 0. |
| 23 | CT_NORMK | Setting of NORMK field in RTL8307h tx cputag when short_dsc_format = 0 |
| 22 | CT_ASPRI | In RTL8307h, setting ASPRI field in tx cputag when short_dsc_format = 0.<br>In RTL8370S, setting priority select field in tx cputag when short_dsc_format =0 |
| 21:18 | CT_SWITCH | Support cputag format of switch<br>0: no cputag support<br>1: 8368<br>2: 8306<br>3: 8307<br>4: 8370<br>5: gmac in 8681.<br>6: gmac in Apollo.<br>8: gmac in ApolloPro |
| 17:16 | CT_RSIZE_1_0 | After rl8681 (including), this field is only for ingress pkt.<br>CTR_size:<br>4h0: 0 Byte<br>4h1: 4 Byte<br>4h2: 8Byte<br>For Apollo cputag with PTP timestamp, set CT_RSIZE to 4h2 |
| 15:8 | CTPM | CPU tag protocol mask.<br>8306:0xf0<br>8368:0xe0<br>8370:0xff<br>8307h:0xff |
| 7:0 | CTPV | CPU tag protocol value.<br>8306:0x90<br>8368:0xa0 or 0xb0<br>8370:0x04<br>8307h:0x04 |

## NIC_CONFIG

*Offset* 0x4c

### Description

Configuration Register?

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:30 | RESERVED ||
| 29:28 | RFF_SIZE_SEL | Set gmac_rxfifo size.<br>2b00: 1KB<br>2b01: 1664B<br>2b10: 2KB |
| 27 | TSO_ID_SEL | Uses to choose LSO(TCP) IP.identification value 0: keep. 1: incremental. |
| 26:25 | RESERVED ||
| 25 | EN_INT_ROUTE | 0: disable interrupt route, IMR0_reg, IMR1_reg<br>1: enable interrupt route, IMR0_reg, IMR1_reg |
| 24 | RX_MULTI_RING_INT_EN | When EN_INT_ROUTE = 0,<br>0: only init.tdu, tok, rok present<br>1: IMR0_reg, IMR1_reg and ISR1_reg present.<br>When EN_INT_ROUTE = 1 this field is 1 |
| 23:22 | RX_SIDEBAND | It is set to 0x3 during init to enable, clear to disable |
| 21:17 | RESERVED ||
| 16 | TX_JUMBO | it is set when tx_jumbo is enabled and cleared when tx_jumbo disabled |
| 15:0 | RESERVED ||

## NIC_CPUTAG1

*Offset* 0x50

### Description

The CPUTAG1 Control Register

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:14 | RESERVED ||
| 13:7 | CT1_SID | It is unkown if it is 7 bits or more but it is set to 64 during so it must be 7 bits at least |
| 6:4 | SPA_DSL | The ingress cputag.SPA=DSL field. Used in RW Apollo cputag. |
| 3 | RESERVED ||
| 2:0 | SPA_PON | The ingress cputag.SPA=PON field. Used in RW Apollo cputag. |

## NIC_MS

*Offset* 0x58

### Description

Media Status Register?

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31 | FORCE_TRXFCE | Force Tx/RX Flow Control:<br>1 = enabled Flow control in the absence of NWAY.<br>0 = disables Flow control in the absence of NWAY.<br>Version effect: rl6166(ECO) and after. |
| 30 | RXFCE | Rx Flow Control Enable |
| 29 | TXFCE | Tx Flow Control Enable:<br>1 = tx flow control enabled.<br>0 = tx flow control disabled.<br>ACCEPT ERROR MUST NOT BE ENABLED |
| 28 | SPEED_1000 | 10: 1000Mbps,<br>11: not allowed |
| 27 | SPEED_10 | 00: 100Mbps,<br>01: 10Mbps |
| 26 | LINKB | Inverse of Link status. 0 = Link OK. 1 = Link Fail |
| 25 | TXPF | Tx Pause frame: 1 = Ethernet module has sent a pause packet. 0 = the Ethernet module has sent a timer done packet |
| 24 | RXPF | Pause Flag: 1 = Ethernet module is in backoff state because a pause packet received. 0 = pause state is clear |
| 23 | SEL_RGMII | gmac_sel_rgmii |
| 22 | FULLDUPREG | Indicates Full duplex mode in gmac |
| 21 | NWCOMPLETE | Nway complete |
| 20 | SEL_MII | indicates in mii mode |
| 19 | FORCEDFULLDUP | force gmac operates at full duplex mode.<br>1b1: force gmac in full duplex mode.<br>1b0: duplex status is from MDIO auto-polling. Not means gmac is in half duplex mode. |
| 18 | FORCELINK | force gmac in link ok mode.<br>This bit is Write only in RLE0315.<br>This bit is R/W in RLE0390 (RL6166).<br>1b1: force gmac in linkok.<br>1b0: link status is from MDIO auto-polling |
| 17:16 | FORCE_SPD | Force gmac in 10/100/GIGA mode.<br>2b00: 100M<br>2b01: 10M<br>2b10: GIGA<br>2b11: not force mode. |
| 15 | SEL_PHYIF_0 | 1: phy interface 0 works.<br>0: phy interface 1 works |
| 14 | RESERVED ||
| 13 | PHY_MODE | 1: in phy mode.<br>0: not in phy mode |
| 12 | RGMII_RX_STS | 0: Does not support rgmii in band status(link status, speed and duplex mode of the PHY) by decoding rxd.<br>1: Supports rgmii in band status(link status, speed and duplex mode of the PHY) by decoding rxd. |
| 11 | RGMII_TX_STS | This field is valid only in phy mode.<br>0: Does not support rgmii in band status(link status, speed and duplex mode of the PHY) by encoding txd.<br>1: Supports rgmii in band status(link status, speed and duplex mode of the PHY) by encoding txd. |
| 10 | FORCE_SPD_MODE | 1: gmac is in force speed mode. The real speed in force mode is set in MS_REG.FORCE_SPD.<br>0: gmac speed status is from md operation. |
| 9:0 | RESERVED ||


## NIC_MIIA

*Offset* 0x5c

### Description

Media Independent Interface Access Register

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31 | FLAG | Flag bit. Set it to 1 to indicate Write flag, set it to 0 to indicate Read flag|
| 30:26 | PHY_ADDR | Defines the Phy address for the MII |
| 23:21 | RESERVED ||
| 22 | DIS_AUTO_POLLING |Disable auto polling feature of mdio operation.<br>0: HW auto polling PCS status.<br>1: HW does not auto polling PCS status|
| 21 | POLLING_EEE | polling PCS EEE advertisement register |
| 20:16 | REG_ADDR_4_0 | 5-bit GMII/MII register address. |
| 15:0 | DATA_15_0 | 16-bit GMII/MII register data. |

## NIC_SWINT

*Offset* 0x60

### Description

Software Interrupt Register

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:1 | RESERVED ||
| 0 | SWINT | Write 1 will force ISR register bit 10 set to 1 |


## NIC_VLAN

*Offset* 0x64

### Description

VLAN Register

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:16 | STAG_PID | Set the s-tag protocol identifier. This field is valid only when COM_REG.TDSC_VLAN_TYPE is high |
| 15 | R_EN_RSTAG |Gmac rx. 0. disable STAG_PID. 1: enable STAG_PID.|
| 14 | R_EN_TSTAG |Gmac tx. 0. disable STAG_PID. 1: enable STAG_PID.|
| 13:0 | RESERVED ||

## NIC_VLAN1

*Offset* 0x68

### Description

VLAN Register

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:16 | STAG_PID1 | Set the s-tag protocol identifier. This field is valid only when COM_REG.TDSC_VLAN_TYPE is high |
| 15 | R_EN_RSTAG |Gmac rx. 0: disable STAG_PID. 1: enable STAG_PID.|
| 14 | R_EN_TSTAG |Gmac tx. 0: disable STAG_PID. 1: enable STAG_PID.|
| 13:0 | RESERVED ||

## NIC_LED_CR

*Offset* 0x70

### Description

LED Control Register

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:20 | RESERVED ||
| 19 | EEE_EN_LED | Enable/disable lpi led. |
| 18 | CUSTOM_LED | Custom led mode. |
| 17:16 | LED_SEL | Non custom led select. Following EEE spec, combine the Link signal and LPI signal in the same LED pin. |
| 15:12 | LED_SEL3 |Custom led3 select|
| 11:8 | LED_SEL2 |Custom led2 select|
| 7:4 | LED_SEL1 |Custom led1 select|
| 3:0 | LED_SEL0 |Custom led0 select|

## NIC_IMR0

*Offset* 0xd0

### Description

Other Interrupt Mask Register

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:29 | RESERVED ||
| 28 | IMR0_TDU5 | Same as IMR0_TDU |
| 27 | IMR0_TDU4 | Same as IMR0_TDU |
| 26 | IMR0_TDU3 | Same as IMR0_TDU |
| 25 | IMR0_TDU2 | Same as IMR0_TDU |
| 24 | IMR0_TDU | Tx Descriptor Unavailable Mask |
| 23:21 | RESERVED ||
| 20 | IMR0_TOK5 | Same as IMR0_TOK |
| 19 | IMR0_TOK4 | Same as IMR0_TDU |
| 18 | IMR0_TOK3 | Same as IMR0_TDU |
| 17 | IMR0_TOK2 | Same as IMR0_TDU |
| 16 | IMR0_TOK | Tx OK Mask |
| 15:6 | RESERVED ||
| 5 | IMR0_RX6 | Some RX Mask |
| 4 | IMR0_RX5 | Some RX Mask |
| 3 | IMR0_RX4 | Some RX Mask |
| 2 | IMR0_RX3 | Some RX Mask |
| 1 | IMR0_RX2 | Some RX Mask |
| 0 | IMR0_RX0 | Some RX Mask |

## NIC_IMR1

*Offset* 0xd4

### Description

Other Other Interrupt Mask Register

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:29 | RESERVED ||
| 28 | IMR1_TDU5 | Same as IMR1_TDU |
| 27 | IMR1_TDU4 | Same as IMR1_TDU |
| 26 | IMR1_TDU3 | Same as IMR1_TDU |
| 25 | IMR1_TDU2 | Same as IMR1_TDU |
| 24 | IMR1_TDU | Tx Descriptor Unavailable Mask |
| 23:21 | RESERVED ||
| 20 | IMR1_TOK5 | Same as IMR1_TOK |
| 19 | IMR1_TOK4 | Same as IMR1_TOK |
| 18 | IMR1_TOK3 | Same as IMR1_TOK |
| 17 | IMR1_TOK2 | Same as IMR1_TOK |
| 16 | IMR1_TOK | Tx OK Mask |

## NIC_ISR1

*Offset* 0xd8

### Description

Other Other Interrupt Status Register

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:29 | RESERVED ||
| 28 | ISR1_TDU5 | Same as ISR1_TDU |
| 27 | ISR1_TDU4 | Same as ISR1_TDU |
| 26 | ISR1_TDU3 | Same as ISR1_TDU |
| 25 | ISR1_TDU2 | Same as ISR1_TDU |
| 24 | ISR1_TDU | Tx Descriptor Unavailable Status |
| 23:21 | RESERVED ||
| 20 | ISR1_TOK5 | Same as ISR1_TOK |
| 19 | ISR1_TOK4 | Same as ISR1_TOK |
| 18 | ISR1_TOK3 | Same as ISR1_TOK |
| 17 | ISR1_TOK2 | Same as ISR1_TOK |
| 16 | ISR1_TOK | Tx OK Status |
| 15:6 | RESERVED ||
| 5 | ISR0_RX6 | Some RX Status |
| 4 | ISR0_RX5 | Some RX Status |
| 3 | ISR0_RX4 | Some RX Status |
| 2 | ISR0_RX3 | Some RX Status |
| 1 | ISR0_RX2 | Some RX Status |
| 0 | ISR0_RX0 | Some RX Status |

## NIC_INTR_REG

*Offset* 0xdc

### Description

It looks like some Interrupt register but it unused nor described in detail.

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:0 | INTR_REG ||

## NIC_TXFPD1

*Offset* 0x1300

### Description

Starting Address of Tx Descriptor 1 (Tx Frame Pointer Descriptor??)

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:0 | TXFDP | Tx First Descriptor Pointer (FDP) for 1st priority RW 0x0 queue |

## NIC_TXCDO1

*Offset* 0x1304

### Description

Tx Current Descriptor Offset?

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:12 | RESERVED ||
| 11:0 | TXCDO | Tx 1st priority Current Descriptor Offset: RO FDP+CDO = current descriptor pointer. CDO increments by 16 bytes each time |

## NIC_TXFPD2

*Offset* 0x1310

### Description

Starting Address of Tx Descriptor 2

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:0 | TXFDP |Tx 2nd priority Descriptor Pointer to the Tx Ring|

## NIC_TXCDO2

*Offset* 0x1314

### Description

Tx Current Descriptor Offset 2?

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:12 | RESERVED ||
| 11:0 | TXCDO |Tx 2nd priority Current Descriptor Offset: FDP+CDO = current descriptor pointer. CDO increments by 16 bytes each time.|

## NIC_TXFPD3

*Offset* 0x1320

### Description

Starting Address of Tx Descriptor 3

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:0 | TXFDP |Tx 3rd priority Descriptor Pointer to the Tx Ring|

## NIC_TXCDO3

*Offset* 0x1324

### Description

Tx Current Descriptor Offset 3?

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:12 | RESERVED ||
| 11:0 | TXCDO |Tx 3rd priority Current Descriptor Offset: FDP+CDO = current descriptor pointer. CDO increments by 16 bytes each time|

## NIC_TXFPD4

*Offset* 0x1330

### Description

Starting Address of Tx Descriptor 4

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:0 | TXFDP |Tx 4th priority Descriptor Pointer to the Tx Ring|

## NIC_TXCDO4

*Offset* 0x1334

### Description

Tx Current Descriptor Offset 4?

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:12 | RESERVED ||
| 11:0 | TXCDO |Tx 4th priority Current Descriptor Offset: RO FDP+CDO = current descriptor pointer. CDO increments by 16 bytes each time|

## NIC_TXFPD5

*Offset* 0x1340

### Description

Starting Address of Tx Descriptor 5

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:0 | TXFDP |Tx 5th priority Descriptor Pointer to the Tx Ring|

## NIC_TXCDO5

*Offset* 0x1344

### Description

Tx Current Descriptor Offset 5?

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:12 | RESERVED ||
| 11:0 | TXCDO |Tx 5th priority Current Descriptor Offset: RO FDP+CDO = current descriptor pointer. CDO increments by 16 bytes each time|

## NIC_RRING_ROUTING1

*Offset* 0x1370

### Description

This is a register for configuring packet internal priority and RX_RING mapping

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:28 | PRI_7_ROUTE | ring assignment for internal priority 7|
| 27:24 | PRI_6_ROUTE | ring assignment for internal priority 6|
| 23:20 | PRI_5_ROUTE | ring assignment for internal priority 5|
| 19:16 | PRI_4_ROUTE | ring assignment for internal priority 4|
| 15:12 | PRI_3_ROUTE | ring assignment for internal priority 3|
| 11:8 | PRI_2_ROUTE | ring assignment for internal priority 2|
| 7:4 | PRI_1_ROUTE | ring assignment for internal priority 1|
| 3:0 | PRI_0_ROUTE | ring assignment for internal priority 0|

## NIC_RRING_ROUTING2

*Offset* 0x1374

### Description

This is a register for configuring packet internal priority and RX_RING mapping

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:28 | PRI_7_ROUTE | ring assignment for internal priority 7|
| 27:24 | PRI_6_ROUTE | ring assignment for internal priority 6|
| 23:20 | PRI_5_ROUTE | ring assignment for internal priority 5|
| 19:16 | PRI_4_ROUTE | ring assignment for internal priority 4|
| 15:12 | PRI_3_ROUTE | ring assignment for internal priority 3|
| 11:8 | PRI_2_ROUTE | ring assignment for internal priority 2|
| 7:4 | PRI_1_ROUTE | ring assignment for internal priority 1|
| 3:0 | PRI_0_ROUTE | ring assignment for internal priority 0|

## NIC_RRING_ROUTING3

*Offset* 0x1378

### Description

This is a register for configuring packet internal priority and RX_RING mapping

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:28 | PRI_7_ROUTE | ring assignment for internal priority 7|
| 27:24 | PRI_6_ROUTE | ring assignment for internal priority 6|
| 23:20 | PRI_5_ROUTE | ring assignment for internal priority 5|
| 19:16 | PRI_4_ROUTE | ring assignment for internal priority 4|
| 15:12 | PRI_3_ROUTE | ring assignment for internal priority 3|
| 11:8 | PRI_2_ROUTE | ring assignment for internal priority 2|
| 7:4 | PRI_1_ROUTE | ring assignment for internal priority 1|
| 3:0 | PRI_0_ROUTE | ring assignment for internal priority 0|

## NIC_RRING_ROUTING4

*Offset* 0x137c

### Description

This is a register for configuring packet internal priority and RX_RING mapping

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:28 | PRI_7_ROUTE | ring assignment for internal priority 7|
| 27:24 | PRI_6_ROUTE | ring assignment for internal priority 6|
| 23:20 | PRI_5_ROUTE | ring assignment for internal priority 5|
| 19:16 | PRI_4_ROUTE | ring assignment for internal priority 4|
| 15:12 | PRI_3_ROUTE | ring assignment for internal priority 3|
| 11:8 | PRI_2_ROUTE | ring assignment for internal priority 2|
| 7:4 | PRI_1_ROUTE | ring assignment for internal priority 1|
| 3:0 | PRI_0_ROUTE | ring assignment for internal priority 0|

## NIC_RRING_ROUTING5

*Offset* 0x1380

### Description

This is a register for configuring packet internal priority and RX_RING mapping

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:28 | PRI_7_ROUTE | ring assignment for internal priority 7|
| 27:24 | PRI_6_ROUTE | ring assignment for internal priority 6|
| 23:20 | PRI_5_ROUTE | ring assignment for internal priority 5|
| 19:16 | PRI_4_ROUTE | ring assignment for internal priority 4|
| 15:12 | PRI_3_ROUTE | ring assignment for internal priority 3|
| 11:8 | PRI_2_ROUTE | ring assignment for internal priority 2|
| 7:4 | PRI_1_ROUTE | ring assignment for internal priority 1|
| 3:0 | PRI_0_ROUTE | ring assignment for internal priority 0|

## NIC_RRING_ROUTING6

*Offset* 0x1384

### Description

This is a register for configuring packet internal priority and RX_RING mapping

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:28 | PRI_7_ROUTE | ring assignment for internal priority 7|
| 27:24 | PRI_6_ROUTE | ring assignment for internal priority 6|
| 23:20 | PRI_5_ROUTE | ring assignment for internal priority 5|
| 19:16 | PRI_4_ROUTE | ring assignment for internal priority 4|
| 15:12 | PRI_3_ROUTE | ring assignment for internal priority 3|
| 11:8 | PRI_2_ROUTE | ring assignment for internal priority 2|
| 7:4 | PRI_1_ROUTE | ring assignment for internal priority 1|
| 3:0 | PRI_0_ROUTE | ring assignment for internal priority 0|

## NIC_RRING_ROUTING7

*Offset* 0x1388

### Description

This is a register for configuring packet internal priority and RX_RING mapping

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:28 | PRI_7_ROUTE | ring assignment for internal priority 7|
| 27:24 | PRI_6_ROUTE | ring assignment for internal priority 6|
| 23:20 | PRI_5_ROUTE | ring assignment for internal priority 5|
| 19:16 | PRI_4_ROUTE | ring assignment for internal priority 4|
| 15:12 | PRI_3_ROUTE | ring assignment for internal priority 3|
| 11:8 | PRI_2_ROUTE | ring assignment for internal priority 2|
| 7:4 | PRI_1_ROUTE | ring assignment for internal priority 1|
| 3:0 | PRI_0_ROUTE | ring assignment for internal priority 0|

## NIC_RXFDP2

*Offset* 0x1390

### Description

Starting Address of Rx Descriptor 1 (Rx Frame Pointer Descriptor??)

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:0 | RXFDP |Rx #2 queue Descriptor Pointer to the Rx Ring |

## NIC_RXCDORINGRS2

*Offset* 0x1394

### Description

Rx Current Descriptor Offset 2 with Ring Size?

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:28 | RESERVED ||
| 27:16 | RXRINGSIZE | The total number of descriptors in the Rx descriptor rings of #2 queue.<br>Act as bit mask, eg. RxRingSize {11:0}:<br>0000_0000_1111: 16 descriptors<br>0000_0001_1111: 32 descriptors<br>0000_0011_1111: 64 descriptors<br>0000_0111_1111: 128 descriptors<br>0000_1111_1111: 256 descriptors<br>0001_1111_1111: 512 descriptors<br>0011_1111_1111: 1024 descriptors<br>0111_1111_1111: 2048 descriptors<br>1111_1111_1111: 4096 descriptors<br>Any other value in this register yields undefined results |
| 15:12 | RESERVED ||
| 11:0 | RXCDO |Rx Current Descriptor Offset of #2 queue: RxFDP+RxCDO = current descriptor pointer. CDO increments by 16 each time (each increment is one byte|

## NIC_RX_CPU_DESN2

*Offset* 0x1398

### Description

Register for Rx CPU Descriptor Number 2???

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:12 | RESERVED ||
| 11:0 | CPU_DES_NUM | Indicate the number of descriptor of #2 queue, which has been finished Rx process and returned to IO by CPU. After ending Rx process, CPU needs to update this field. |

## NIC_RX_DES_THRES2

*Offset* 0x139c

### Description

Register for the Rx Descriptor Threshold 2

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:28 | RESERVED ||
| 27:16 | DES_ON_TH | Specifies the difference between EthrnetRxCPU_Des_Num2 and the descriptor #2of #2 queue currently in use by Ethernet Module in which flow control will be assert |
| 15:12 | RESERVED ||
| 11:0 | DES_OFF_TH | Specifies the difference between EthrnetRxCPU_Des_Num2 and the descriptor #2 of 2#2queue currently in use by Ethernet Module in which flow control will be de-assert |

## NIC_RXFDP3

*Offset* 0x13a0

### Description

Starting Address of Rx Descriptor 3

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:0 | RXFDP |Rx # 3 queue Descriptor Pointer to the Rx Ring|

## NIC_RXCDORINGRS3

*Offset* 0x13a4

### Description

Rx Current Descriptor Offset 3 with Ring Size?

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:28 | RESERVED ||
| 27:16 | RXRINGSIZE | The total number of descriptors in the Rx descriptor rings of #3 queue. |
| 15:12 | RESERVED ||
| 11:0 | RXCDO |Rx Current Descriptor Offset of #3 queue: RxFDP+RxCDO = current descriptor pointer. CDO increments by 16 each time (each increment is one byte|

## NIC_RX_CPU_DESN3

*Offset* 0x13a8

### Description

Register for Rx CPU Descriptor Number 3???

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:12 | RESERVED ||
| 11:0 | CPU_DES_NUM | Indicate the number of descriptor of #3 queue, which has been finished Rx process and returned to IO by CPU. After ending Rx process, CPU needs to update this field. |

## NIC_RX_DES_THRES3

*Offset* 0x13ac

### Description

Register for the Rx Descriptor Threshold 3

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:28 | RESERVED ||
| 27:16 | DES_ON_TH | Specifies the difference between EthrnetRxCPU_Des_Num3 and the descriptor #3 of #3 queue currently in use by Ethernet Module in which flow control will be assert |
| 15:12 | RESERVED ||
| 11:0 | DES_OFF_TH | Specifies the difference between EthrnetRxCPU_Des_Num3 and the descriptor #3of #3 queue currently in use by Ethernet Module in which flow control will be de-assert |

## NIC_RXFDP4

*Offset* 0x13b0

### Description

Starting Address of Rx Descriptor 4

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:0 | RXFDP |Rx 4 queue Descriptor Pointer to the Rx Ring|

## NIC_RXCDORINGRS4

*Offset* 0x13b4

### Description

Rx Current Descriptor Offset 4 with Ring Size?

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:28 | RESERVED ||
| 27:16 | RXRINGSIZE | The total number of descriptors in the Rx descriptor rings of #4 queue. |
| 15:12 | RESERVED ||
| 11:0 | RXCDO |Rx Current Descriptor Offset of #4 queue: RxFDP+RxCDO = current descriptor pointer. CDO increments by 16 each time (each increment is one byte|

## NIC_RX_CPU_DESN4

*Offset* 0x13b8

### Description

Register for Rx CPU Descriptor Number 4???

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:12 | RESERVED ||
| 11:0 | CPU_DES_NUM | Indicate the number of descriptor of #4 queue, which has been finished Rx process and returned to IO by CPU. After ending Rx process, CPU needs to update this field. |

## NIC_RX_DES_THRES4

*Offset* 0x13bc

### Description

Register for the Rx Descriptor Threshold 4

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:28 | RESERVED ||
| 27:16 | DES_ON_TH | Specifies the difference between EthrnetRxCPU_Des_Num4 and the descriptor #4 of #4 queue currently in use by Ethernet Module in which flow control will be assert |
| 15:12 | RESERVED ||
| 11:0 | DES_OFF_TH | Specifies the difference between EthrnetRxCPU_Des_Num4 and the descriptor #4of #4 queue currently in use by Ethernet Module in which flow control will be de-assert |

## NIC_RXFDP5

*Offset* 0x13c0

### Description

Starting Address of Rx Descriptor 5

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:0 | RXFDP |Rx 5 queue Descriptor Pointer to the Rx Ring|

## NIC_RXCDORINGRS5

*Offset* 0x13c4

### Description

Rx Current Descriptor Offset 5 with Ring Size?

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:28 | RESERVED ||
| 27:16 | RXRINGSIZE | The total number of descriptors in the Rx descriptor rings of #5 queue. |
| 15:12 | RESERVED ||
| 11:0 | RXCDO |Rx Current Descriptor Offset of #5 queue: RxFDP+RxCDO = current descriptor pointer. CDO increments by 16 each time (each increment is one byte|

## NIC_RX_CPU_DESN5

*Offset* 0x13c8

### Description

Register for Rx CPU Descriptor Number 5???

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:12 | RESERVED ||
| 11:0 | CPU_DES_NUM | Indicate the number of descriptor of #5 queue, which has been finished Rx process and returned to IO by CPU. After ending Rx process, CPU needs to update this field. |

## NIC_RX_DES_THRES5

*Offset* 0x13cc

### Description

Register for the Rx Descriptor Threshold 5

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:28 | RESERVED ||
| 27:16 | DES_ON_TH | Specifies the difference between EthrnetRxCPU_Des_Num5 and the descriptor #5 of #5 queue currently in use by Ethernet Module in which flow control will be assert |
| 15:12 | RESERVED ||
| 11:0 | DES_OFF_TH | Specifies the difference between EthrnetRxCPU_Des_Num5 and the descriptor #5 of #5 queue currently in use by Ethernet Module in which flow control will be de-assert |

## NIC_RXFDP6

*Offset* 0x13d0

### Description

Starting Address of Rx Descriptor 6

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:0 | RXFDP |Rx 6 queue Descriptor Pointer to the Rx Ring|

## NIC_RXCDORINGRS6

*Offset* 0x13d4

### Description

Rx Current Descriptor Offset 6 with Ring Size?

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:28 | RESERVED ||
| 27:16 | RXRINGSIZE | The total number of descriptors in the Rx descriptor rings of #6 queue. |
| 15:12 | RESERVED ||
| 11:0 | RXCDO |Rx Current Descriptor Offset of #6 queue: RxFDP+RxCDO = current descriptor pointer. CDO increments by 16 each time (each increment is one byte|

## NIC_RX_CPU_DESN6

*Offset* 0x13d8

### Description

Register for Rx CPU Descriptor Number 6???

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:12 | RESERVED ||
| 11:0 | CPU_DES_NUM | Indicate the number of descriptor of #6 queue, which has been finished Rx process and returned to IO by CPU. After ending Rx process, CPU needs to update this field. |

## NIC_RX_DES_THRES6

*Offset* 0x13dc

### Description

Register for the Rx Descriptor Threshold 6

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:28 | RESERVED ||
| 27:16 | DES_ON_TH | Specifies the difference between EthrnetRxCPU_Des_Num6 and the descriptor #6 of #6 queue currently in use by Ethernet Module in which flow control will be assert |
| 15:12 | RESERVED ||
| 11:0 | DES_OFF_TH | Specifies the difference between EthrnetRxCPU_Des_Num6 and the descriptor #6 of #6 queue currently in use by Ethernet Module in which flow control will be de-assert |

## NIC_RXFDP1

*Offset* 0x13f0

### Description

Starting Address of Rx Descriptor 1

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:0 | RXFDP |Rx 1st queue Descriptor Pointer to the Rx Ring|

## NIC_RXCDORINGRS1

*Offset* 0x13f4

### Description

Rx Current Descriptor Offset 1 with Ring Size?

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:28 | RESERVED ||
| 27:16 | RXRINGSIZE | This is the total number of descriptors in the Rx descriptor rings of 1st queue |
| 15:12 | RESERVED ||
| 11:0 | RXCDO |Rx Current Descriptor Offset of 1st queue: RxFDP+RxCDO = current descriptor pointer. CDO increments by 16 each time (each increment is one byte).|

## NIC_SMSA

*Offset* 0x13fc

### Description

SRAM mapping start address register

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:0 | SMSA |SRAM mapping start address for header mapping to sram|

## NIC_PROBE_SELECT

*Offset* 0x1400 - assumption

### Description

It is not mentioned in `re8686_rtl9607c` files at all

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:26 | RESERVED ||
| 25:24 | PROB_SELf |This MAC IP will have 16 probe signal output for debug. These 2 bit choose between 4 sets of internal signal being probed.|
| 23:9 | RESERVED ||

## NIC_DIAGNOSE1

*Offset* 0x1404

### Description

Register for Diagnostic enable?

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:6 | RESERVED ||
| 5:3 | RXMRING ||
| 2:0 | LSO_STS ||

## NIC_RX_PSE1_TXC_OUT_SEL1

*Offset* 0x142c

### Description

Some register for Rx flow control descriptor threshold 

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:10 | RESERVED ||
| 27:24 | DES_OFF_TH_11_8 | Specifies the difference between EthrnetRxCPU_Des_Num1 and the descriptor # of 1st queue currently in use by Ethernet Module in which flow control will be de-assert. Bits 11:8 |
| 9 | SET_D_TXC ||
| 8:4 | TXC_OUT_PH_SEL ||
| 3:0 | RX_TH_OFF_1 ||

## NIC_ETNRXCPU1

*Offset* 0x1430

### Description

Register for Rx CPU Descriptor Number and Descriptor Threshold 1

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:23 | CPU_DES_NUM_7_0 | Indicate the number of descriptor of 1st queue, which has been finished Rx process and returned to IO by CPU. After ending Rx process, CPU needs to update this field. Bits 7:0 |
| 23:16 | DES_ON_TH_7_0 | Specifies the difference between EthrnetRxCPU_Des_Num1 and the descriptor # of 1st queue currently in use by Ethernet Module in which flow control will be assert. Bits 7:0 |
| 15:8 | DES_OFF_TH_7_0 | Specifies the difference between EthrnetRxCPU_Des_Num1 and the descriptor # of 1st queue currently in use by Ethernet Module in which flow control will be de-assert. Bits 7:0 |
| 7:4 | CPU_DES_NUM_11_8 | Indicate the number of descriptor of 1st queue, which has been finished Rx process and returned to IO by CPU. After ending Rx process, CPU needs to update this field. Bits 11:8 |
| 3:0 | DES_ON_TH_11_8 | Specifies the difference between EthrnetRxCPU_Des_Num1 and the descriptor # of 1st queue currently in use by Ethernet Module in which flow control will be assert. Bits 11:8 |

## NIC_ETN_IO_CMD

*Offset* 0x1434

### Description

IO Command/Control Register

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31 | MAX_DMA_SEL_0 |Select the dma burst size on bus(memory controller should assert continuous btrdy).<br>00:16 DW(1DW=4B)<br>01:32 DW<br>10:64 DW|
| 30 | SHORT_DES_FMT |Short descriptor format. Set 1 tx/rx descriptor will use old format - 4x32bit each item, set 0 use new format to support sram mapping.|
| 29 | MAX_DMA_SEL_1 ||
| 28 | EN_EARLY_TX |0: disable, 1: enable. Disable early tx by GAMC while tx command descriptor.IPCS, UDPCS or TCPCS are set to high|
| 27:24 | TX_PKT_TMR | Timer to trigger TxOK interrupt after receipt of TxIntMitigation pkts. 0000 no timer set<br>0001-1111 : the timer interval defining a multiple of TU |
| 23 | TX_INT_MITIG_3 ||
| 22 | RX_PKT_TMR_3 ||
| 21 | RX_INT_MITIG_3 ||
| 20:19 | TSH |Tx Threshold: Specifies the threshold level in the Tx FIFO to begin the transmission. When the byte count of the data in the Tx FIFO reaches this level, (or the FIFO contains at least one complete packet or the end of a packet) the Ethernet module will transmit this packet.<br>00:128B.<br>01:256B.<br>10:512B.<br>11:1024B.|
| 18:16 | TX_INT_MITIG_2_0 |This sets the number of packets received before TxOK interrupt is triggered.<br>0000- 1 pkt<br>0001- 4 pkts<br>0010- 8 pkts<br>0011- 12 pkts<br>0100- 16 pkts<br>0101- 20 pkts<br>0110- 24 pkts<br>0111- 28 pkts|
| 15:13 | RX_PKT_TMR_2_0 | Timer to trigger RxOK interrupt after receipt of RxIntMitigation pkts.<br>0000 no timer set<br>0001-1111 : the timer interval defining a multiple of TU |
| 12:11 | RXFTH | Rx Threshold: Specifies the threshold level in the Rx FIFO to begin the transmission. When the byte count of the data in the Rx FIFO reaches this level, (or the FIFO contains at least one complete packet or the end of a packet) the Ethernet module will transmit this packet.<br>00 256 bytes<br>10 64 bytes<br>11 128 bytes |
| 10:8 | RX_INT_MITIG_2_0 |This sets the number of packets received before RxOK interrupt is triggered.<br>0000- 1 pkt<br>0001- 4 pkts<br>0010- 8 pkts<br>0011- 12 pkts<br>0100- 16 pkts<br>0101- 20 pkts<br>0110- 24 pkts<br>0111- 28 pkts|
| 7:6 | REG_INI_TMR_SEL |RXPktTimer, TXPktTimer Unit. (TU)| 
| 5 | RE | MII Rx Enable |
| 4 | TE | MII Tx Enable |
| 3 | TXFN4 | 4th Priority DMA-Ethernet Transmit enable.<br>1: Enable.<br>0: Disable |
| 2 | TXFN3 | 3rd Priority DMA-Ethernet Transmit enable.<br>1: Enable.<br>0: Disable |
| 1 | TXFN2 | 2nd Priority DMA-Ethernet Transmit enable.<br>1: Enable.<br>0: Disable |
| 0 | TXFN1 | 1st Priority DMA-Ethernet Transmit enable.<br>1: Enable.<br>0: Disable |

## NIC_ETN_IO_CMD1

*Offset* 0x1438

### Description

The Other IO Command/Control Register 

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31 | RESERVED ||
| 28:26 | DSC_FMT_EXTRA | Extra descriptor format.<br>Dsc_format_extra{0} used to indicate the lso format in tx descriptor.<br>In rle0437, bit28 is lso_des_format and is write only. |
| 26 | RXOKINT_MSK_128B |1: For ingress pkt which is short than 128B, RxOK interrupt asserts after DMA completes(compatible issue).<br>0: For ingress pkt which is short than 128B, RxOK interrupt does not assert after DMA completes.|
| 25 | EN_RX_MRING | Enable rx multiple rings.<br>1: rx using multiple rings. max: 6rings (ring1 to ring6).<br>0. rx using single ring.|
| 24 | EN_1GB |1: support 1GB addressing in lx master bus. For gmac used in rl0371 and after.<br>0: no support. For project used in rle0390 and before|
| 23:22 | RESERVED ||
| 21 | RXRING6 | Ethernet-DMA Receive Ring6 enable.<br>1: Enable.<br>0: Disable |
| 20 | RXRING5 | Ethernet-DMA Receive Ring5 enable |
| 19 | RXRING4 | Ethernet-DMA Receive Ring4 enable |
| 18 | RXRING3 | Ethernet-DMA Receive Ring3 enable |
| 17 | RXRING2 | Ethernet-DMA Receive Ring2 enable |
| 16 | RXRING1 | Ethernet-DMA Receive Ring1 enable |
| 15:14 | TX_HL_PRI_SEL | 2b00: TX ring uses strict priority.<br>2b01: TX ring uses high and low queue priority. Inside high queue, tx ring is round robin. Inside low queue, tx ring is round robin. Strict priority is used for high and low queue selection.<br>2b10 and 2b11: reserved. |
| 13:9 | RESERVED ||
| 8 | TX_FN5 | 5th Priority DMA-Ethernet Transmit enable.<br>1: Enable.<br>0: Disable.<br>After IO_CMD.TE is set high, TxFN5th is writable. |
| 7:5 | RESERVED ||
| 4 | TXQ5_H |1: TxFN5th is a high queue.<br>0: TxFN5th is a low queue|
| 3 | TXQ4_H |1: TxFN4th is a high queue.<br>0: TxFN4th is a low queue|
| 2 | TXQ3_H |1: TxFN3rd is a high queue.<br>0: TxFN3rd is a low queue|
| 1 | TXQ2_H |1: TxFN2nd is a high queue.<br>0: TxFN2nd is a low queue|
| 0 | TXQ1_H |1: TxFN1st is a high queue.<br>0: TxFN1st is a low queue|

## NIC_WOL

*Offset* 0x143c - assumption

### Description

It is not mentioned in `re8686_rtl9607c` files at all. Wake on LAN Register?

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:3 | RESERVED ||
| 2 | WOL_PME |0: No magic pkt receives. 1: HW had received one magic pkt and system should wake up|
| 1 | WOL_STS |0: HW is not in wol idle state. 1: HW is in wol idle state.|
| 0 | WOL_CMD |Issue wol command by SW|
