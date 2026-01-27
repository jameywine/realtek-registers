
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
| 31 | ISR_RDU6 | Same as ISR_RDU |
| 30 | ISR_RDU5 | Same as ISR_RDU |
| 29 | ISR_RDU4 | Same as ISR_RDU |
| 28 | ISR_RDU3 | Same as ISR_RDU |
| 27 | ISR_RDU2 | Same as ISR_RDU |
| 26 | ISR_SW_INT | Software Interrupt Mask |
| 25 | ISR_TDU | Tx Descriptor Unavailable: When set, this bit indicates that the Tx descriptor is unavailable.|
| 24 | ISR_LINK_CHG | Link Change: This bit is set to 1 when link status is changed.|
| 23 | ISR_TER | Transmit (Tx) Error: This bit set to 1 indicates that a packet transmission was aborted, due to excessive collisions. |
| 22 | ISR_TOK_TI ||
| 21 | ISR_RDU | Rx Descriptor Unavailable 1: When set to 1, this bit indicates that the Rx descriptor is unavailable.|
| 20 | ISR_RER_OVF | Receive (Rx) Overflow Error |
| 19 | RESERVED ||
| 18 | ISR_RER_RUNT | Receive (Rx) Runt Error |
| 17 | RESERVED ||
| 16 | ISR_ROK | Receive (Rx) OK: In normal mode, this bit set to 1 indicates the successful completion of a packet reception. |
| 15 | IMR_RDU6 | Same as IMR_RDU |
| 14 | IMR_RDU5 | Same as IMR_RDU |
| 13 | IMR_RDU4 | Same as IMR_RDU |
| 12 | IMR_RDU3 | Same as IMR_RDU |
| 11 | IMR_RDU2 | Same as IMR_RDU |
| 10 | IMR_SW_INT | Software Interrupt 1: Enable. 0: Disable. |
| 9 | IMR_TDU | Tx Descriptor Unavailable Interrupt 1: Enable. 0: Disable. |
| 8 | IMR_LINK_CHG | Link Change Interrupt 1: Enable, 0: Disable. |
| 7 | IMR_TER | Transmit (Tx) Error Enable: 1: Enable. 0: Disable. |
| 6 | IMR_TOK_TI ||
| 5 | IMR_RDU | Rx Descriptor Unavailable Interrupt 1: 1: Enable. 0: Disable.|
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
| 7 | HOME_PNA ||
| 6 | AFLOW ||
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
| 31 | CTEN_RX | It is set to 1 during init |
| 27:24 | CT_TSIZE | It is set to 0x2 during init |
| 25:24 | CT_RSIZE_3_2 ||
| 24 | CT_DSLRN ||
| 23 | CT_NORMK ||
| 22 | CT_ASPRI ||
| 21:18 | CT_SWITCH | It is set to 0x8 during init |
| 17:16 | CT_RSIZE_1_0 | It is set to 0x2 during init |
| 15:8 | CTPM | It is set to 0xff during init and has these variations: CTPM_8370: 0xff, CTPM_8368: 0xe0, CTPM_8306: 0xf0 |
| 7:0 | CTPV | It is set to 0x04 during init and has these variations: CTPV_8370: 0x04, CTPV_8368: 0xa0, CTPV_8306: 0x90 |

## NIC_CONFIG

*Offset* 0x4c

### Description

Configuration Register?

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:30 | RESERVED ||
| 29:28 | RFF_SIZE_SEL | it is set to 0x2 during init|
| 27 | TSO_ID_SEL ||
| 26:25 | RESERVED ||
| 24 | RX_MULTI_RING_INT_EN | It is set to enable rx multi ring interrupt? |
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
| 6:4 | SPA_DSL ||
| 3 | RESERVED ||
| 2:0 | SPA_PON ||

## NIC_MS

*Offset* 0x54

### Description

Media Status Register?

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31 | FORCE_TRXFCE ||
| 30 | RXFCE | Rx Flow Control Enable |
| 29 | TXFCE | Tx Flow Control Enable |
| 28 | SPEED_1000 | Link speed is 1000Mbps |
| 27 | SPEED_10 | Link speed is 10Mbps |
| 26 | LINKB | Link Status Bit |
| 25 | TXPF ||
| 24 | RXPF ||
| 23 | SEL_RGMII ||
| 22 | FULLDUPREG ||
| 21 | NWCOMPLETE ||
| 20 | SEL_MII ||
| 19 | FORCEDFULLDUP ||
| 18 | FORCELINK ||
| 17:16 | FORCE_SPD ||
| 15 | SEL_PHYIF_0 ||
| 14 | RESERVED ||
| 13 | PHY_MODE ||
| 12 | RGMII_RX_STS ||
| 11 | RGMII_TX_STS ||
| 10 | FORCE_SPD_MODE ||
| 9:0 | RESERVED ||


## NIC_MIIA

*Offset* 0x58

### Description

Media Independent Interface Access Register

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31 | FLAG | Flag bit. Set it to 1 to indicate Write flag, set it to 0 to indicate Read flag|
| 30:26 | PHY_ADDR | 5-bit PHY address |
| 23:21 | RESERVED ||
| 22 | DIS_AUTO_POLLING ||
| 21 | POLLING_EEE ||
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
| 0 | SWINT | Software Interrupt |


## NIC_VLAN

*Offset* 0x60

### Description

VLAN Register

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:16 | STAG_PID ||
| 15 | TDSC_VLAN_TYPE ||
| 14:0 | RESERVED ||

## NIC_LED_CR

*Offset* 0x70

### Description

LED Control Register

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:20 | RESERVED ||
| 19 | EEE_EN_LED ||
| 18 | CUSTOM_LED ||
| 17:16 | LED_SEL ||
| 15:12 | LED_SEL3 ||
| 11:8 | LED_SEL2 ||
| 7:4 | LED_SEL1 ||
| 3:0 | LED_SEL0 ||

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
| 31:0 | TXFDP ||

## NIC_TXCDO1

*Offset* 0x1304

### Description

Tx Current Descriptor Offset?

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:12 | RESERVED ||
| 11:0 | TXCDO ||

## NIC_TXFPD2

*Offset* 0x1310

### Description

Starting Address of Tx Descriptor 2

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:0 | TXFDP ||

## NIC_TXCDO2

*Offset* 0x1314

### Description

Tx Current Descriptor Offset 2?

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:12 | RESERVED ||
| 11:0 | TXCDO ||

## NIC_TXFPD3

*Offset* 0x1320

### Description

Starting Address of Tx Descriptor 3

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:0 | TXFDP ||

## NIC_TXCDO3

*Offset* 0x1324

### Description

Tx Current Descriptor Offset 3?

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:12 | RESERVED ||
| 11:0 | TXCDO ||

## NIC_TXFPD4

*Offset* 0x1330

### Description

Starting Address of Tx Descriptor 4

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:0 | TXFDP ||

## NIC_TXCDO4

*Offset* 0x1334

### Description

Tx Current Descriptor Offset 4?

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:12 | RESERVED ||
| 11:0 | TXCDO ||

## NIC_TXFPD5

*Offset* 0x1340

### Description

Starting Address of Tx Descriptor 5

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:0 | TXFDP ||

## NIC_TXCDO5

*Offset* 0x1344

### Description

Tx Current Descriptor Offset 5?

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:12 | RESERVED ||
| 11:0 | TXCDO ||

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
| 31:0 | RXFDP ||

## NIC_RXCDORINGRS2

*Offset* 0x1394

### Description

Rx Current Descriptor Offset 2 with Ring Size?

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:28 | RESERVED ||
| 27:16 | RXRINGSIZE | Rx Ring Size |
| 15:12 | RESERVED ||
| 11:0 | RXCDO ||

## NIC_RX_CPU_DESN2

*Offset* 0x1398

### Description

Register for Rx CPU Descriptor Number 2???

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:12 | RESERVED ||
| 11:0 | CPU_DES_NUM | Rx Descriptor Number? |

## NIC_RX_DES_THRES2

*Offset* 0x139c

### Description

Register for the Rx Descriptor Threshold 2

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:28 | RESERVED ||
| 27:16 | DES_ON_TH | flow control assert threshold: available desc <= 16 |
| 15:12 | RESERVED ||
| 11:0 | DES_OFF_TH | flow control de-assert threshold : available desc>=48 |

## NIC_RXFDP3

*Offset* 0x13a0

### Description

Starting Address of Rx Descriptor 3

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:0 | RXFDP ||

## NIC_RXCDORINGRS3

*Offset* 0x13a4

### Description

Rx Current Descriptor Offset 3 with Ring Size?

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:28 | RESERVED ||
| 27:16 | RXRINGSIZE | Rx Ring Size |
| 15:12 | RESERVED ||
| 11:0 | RXCDO ||

## NIC_RX_CPU_DESN3

*Offset* 0x13a8

### Description

Register for Rx CPU Descriptor Number 3???

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:12 | RESERVED ||
| 11:0 | CPU_DES_NUM | Rx Descriptor Number? |

## NIC_RX_DES_THRES3

*Offset* 0x13ac

### Description

Register for the Rx Descriptor Threshold 3

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:28 | RESERVED ||
| 27:16 | DES_ON_TH | flow control assert threshold: available desc <= 16 |
| 15:12 | RESERVED ||
| 11:0 | DES_OFF_TH | flow control de-assert threshold : available desc>=48 |

## NIC_RXFDP4

*Offset* 0x13b0

### Description

Starting Address of Rx Descriptor 4

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:0 | RXFDP ||

## NIC_RXCDORINGRS4

*Offset* 0x13b4

### Description

Rx Current Descriptor Offset 4 with Ring Size?

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:28 | RESERVED ||
| 27:16 | RXRINGSIZE | Rx Ring Size |
| 15:12 | RESERVED ||
| 11:0 | RXCDO ||

## NIC_RX_CPU_DESN4

*Offset* 0x13b8

### Description

Register for Rx CPU Descriptor Number 4???

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:12 | RESERVED ||
| 11:0 | CPU_DES_NUM | Rx Descriptor Number? |

## NIC_RX_DES_THRES4

*Offset* 0x13bc

### Description

Register for the Rx Descriptor Threshold 4

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:28 | RESERVED ||
| 27:16 | DES_ON_TH | flow control assert threshold: available desc <= 16 |
| 15:12 | RESERVED ||
| 11:0 | DES_OFF_TH | flow control de-assert threshold : available desc>=48 |

## NIC_RXFDP5

*Offset* 0x13c0

### Description

Starting Address of Rx Descriptor 5

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:0 | RXFDP ||

## NIC_RXCDORINGRS5

*Offset* 0x13c4

### Description

Rx Current Descriptor Offset 5 with Ring Size?

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:28 | RESERVED ||
| 27:16 | RXRINGSIZE | Rx Ring Size |
| 15:12 | RESERVED ||
| 11:0 | RXCDO ||

## NIC_RX_CPU_DESN5

*Offset* 0x13c8

### Description

Register for Rx CPU Descriptor Number 5???

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:12 | RESERVED ||
| 11:0 | CPU_DES_NUM | Rx Descriptor Number? |

## NIC_RX_DES_THRES5

*Offset* 0x13cc

### Description

Register for the Rx Descriptor Threshold 5

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:28 | RESERVED ||
| 27:16 | DES_ON_TH | flow control assert threshold: available desc <= 16 |
| 15:12 | RESERVED ||
| 11:0 | DES_OFF_TH | flow control de-assert threshold : available desc>=48 |

## NIC_RXFDP6

*Offset* 0x13d0

### Description

Starting Address of Rx Descriptor 6

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:0 | RXFDP ||

## NIC_RXCDORINGRS6

*Offset* 0x13d4

### Description

Rx Current Descriptor Offset 6 with Ring Size?

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:28 | RESERVED ||
| 27:16 | RXRINGSIZE | Rx Ring Size |
| 15:12 | RESERVED ||
| 11:0 | RXCDO ||

## NIC_RX_CPU_DESN6

*Offset* 0x13d8

### Description

Register for Rx CPU Descriptor Number 6???

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:12 | RESERVED ||
| 11:0 | CPU_DES_NUM | Rx Descriptor Number? |

## NIC_RX_DES_THRES6

*Offset* 0x13dc

### Description

Register for the Rx Descriptor Threshold 6

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:28 | RESERVED ||
| 27:16 | DES_ON_TH | flow control assert threshold: available desc <= 16 |
| 15:12 | RESERVED ||
| 11:0 | DES_OFF_TH | flow control de-assert threshold : available desc>=48 |

## NIC_RXFDP1

*Offset* 0x13f0

### Description

Starting Address of Rx Descriptor 1

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:0 | RXFDP ||

## NIC_RXCDORINGRS1

*Offset* 0x13f4

### Description

Rx Current Descriptor Offset 1 with Ring Size?

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:28 | RESERVED ||
| 27:16 | RXRINGSIZE | Rx Ring Size |
| 15:12 | RESERVED ||
| 11:0 | RXCDO ||

## NIC_SMSA

*Offset* 0x13fc

### Description

Unused register

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:0 | SMSA ||

## NIC_PROBE_SELECT

*Offset* 0x1400 - assumption

### Description

It is not mentioned in `re8686_rtl9607c` files at all

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:26 | RESERVED ||
| 25:24 | PROB_SELf ||
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
| 27:24 | DES_OFF_TH_11_8 | Descriptor Off Threshold Bits 11-8 |
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
| 31:23 | CPU_DES_NUM_7_0 | CPU Descriptor Number Bits 7-0 |
| 23:16 | DES_ON_TH_7_0 | Descriptor On Threshold Bits 7-0 |
| 15:8 | DES_OFF_TH_7_0 | Descriptor Off Threshold Bits 7-0 |
| 7:4 | CPU_DES_NUM_11_8 | CPU Descriptor Number Bits 11-8 |
| 3:0 | DES_ON_TH_11_8 | Descriptor On Threshold Bits 11-8 |

## NIC_ETN_IO_CMD

*Offset* 0x1434

### Description

IO Command/Control Register

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31 | MAX_DMA_SEL_0 ||
| 30 | SHORT_DES_FMT ||
| 29 | MAX_DMA_SEL_1 ||
| 28 | EN_EARLY_TX ||
| 27:24 | TX_PKT_TMR | Tx Packet Timer|
| 23 | TX_INT_MITIG_3 ||
| 22 | RX_PKT_TMR_3 ||
| 21 | RX_INT_MITIG_3 ||
| 20:19 | TSH |Threshold for TX FIFO?|
| 18:16 | TX_INT_MITIG_2_0 ||
| 15:13 | RX_PKT_TMR_2_0 | Rx Packet Timer |
| 12:11 | RXFTH | Rx FIFO Threshold |
| 10:8 | RX_INT_MITIG_2_0 ||
| 7:6 | REG_INI_TMR_SEL || 
| 5 | RE | Receiver Enable |
| 4 | TE | Transmitter Enable |
| 3 | TXFN4 | TX Poll Kick 4 |
| 2 | TXFN3 | TX Poll Kick 3 |
| 1 | TXFN2 | TX Poll Kick 2 |
| 0 | TXFN1 | TX Poll Kick 1 |

## NIC_ETN_IO_CMD1

*Offset* 0x1438

### Description

The Other IO Command/Control Register 

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31 | RESERVED ||
| 28:26 | DSC_FMT_EXTRA | It is set to 0x3 during init |
| 26 | RXOKINT_MSK_128B ||
| 25 | EN_RX_MRING | Enable Rx Multi Ring?|
| 24 | EN_1GB ||
| 23:22 | RESERVED ||
| 21 | RXRING6 | Enable RX Ring 6? |
| 20 | RXRING5 | Enable RX Ring 5? |
| 19 | RXRING4 | Enable RX Ring 4? |
| 18 | RXRING3 | Enable RX Ring 3? |
| 17 | RXRING2 | Enable RX Ring 2? |
| 16 | RXRING1 | Enable RX Ring 1? |
| 15 | RESERVED ||
| 14 | TX_RR_SCHEDULER | Sets TX Ring Priority in RR |
| 13:9 | RESERVED ||
| 8 | TX_FN5 | TX Poll Kick 5 |
| 7:5 | RESERVED ||
| 4 | TXQ5_H ||
| 3 | TXQ4_H ||
| 2 | TXQ3_H ||
| 1 | TXQ2_H ||
| 0 | TXQ1_H ||

## NIC_WOL

*Offset* 0x143c - assumption

### Description

It is not mentioned in `re8686_rtl9607c` files at all. Wake on LAN Register?

### Fields

| Bit(s) | Field Name | Description |
| :--- | :--- | :--- |
| 31:3 | RESERVED ||
| 2 | WOL_PME ||
| 1 | WOL_STS ||
| 0 | WOL_CMD ||
