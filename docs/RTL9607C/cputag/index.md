---
tags:
  - RTL9607C
  - CPU Tags
---

# RTL9607C CPU tags

## Frame direction:  RX

|Name|LSB|Bits|Description|
| :--- | :--- | :--- | :--- |
|own|0|1||
|eor|1|1||
|fs|2|1||
|ls|3|1||
|crcerr|4|1||
|ipv4csf|5|1||
|l4csf|6|1||
|rcdf|7|1||
|ipfrag|8|1||
|pppoetag|9|1||
|rwt|10|1||
|rsvd1|11|7||
|data_length|18|14||
|cputag|32|1||
|ptp_in_cpu_tag_exist|33|1||
|svlan_tag_exist|34|1||
|reason|35|8||
|rsvd_1|43|4||
|ctagva|47|1||
|cvlan_tag|48|16||
|internal_priority|64|3||
|pon_sid_or_extspa|67|7||
|l3routing|74|1||
|origformat|75|1||
|src_port_num|76|4||
|fbi|80|1||
|fb_hash_or_dst_portmsk|81|15||

## Frame direction:  TX

|Name|LSB|Bits|Description|
| :--- | :--- | :--- | :--- |
|own|0|1||
|eor|1|1||
|fs|2|1||
|ls|3|1||
|ipcs|4|1||
|l4cs|5|1||
|tpid_sel|6|1||
|stag_aware|7|1||
|crc|8|1||
|rsvd|9|6||
|data_length|15|17||
|cputag|32|1||
|tx_svlan_action|33|2||
|tx_cvlan_action|35|2||
|tx_portmask|37|11||
|cvlan_vidl|48|8||
|cvlan_prio|56|3||
|cvlan_cfi|59|1||
|cvlan_vidh|60|4||
|rsvd1|64|4||
|aspri|68|1||
|cputag_pri|69|3||
|keep|72|1||
|rsvd2|73|1||
|dislrn|74|1||
|cputag_psel|75|1||
|gmac_id|76|2||
|l34_keep|78|1||
|rsvd3|79|1||
|extspa|80|3||
|tx_pppoe_action|83|2||
|tx_pppoe_idx|85|4||
|tx_dst_stream_id|89|7||
|lgsen|96|1||
|lgmtu|97|11||
|rsvd|108|4||
|svlan_vidl|112|8||
|svlan_prio|120|3||
|svlan_cfi|123|1||
|svlan_vidh|124|4||
