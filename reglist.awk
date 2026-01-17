#if defined(CONFIG_SDK_CHIP_FEATURE_INTERFACE)
#if defined(CONFIG_SDK_RTL9607C)
#    {
#        #if defined(CONFIG_SDK_DUMP_REG_WITH_NAME)
#        /* register name  */    "DIGITAL_INTERFACE_SELECT",
#        #endif  /* CONFIG_SDK_DUMP_REG_WITH_NAME */
#        /* offset address */    0x23000,
#        /* field numbers */     3,
#        /* array offset */      0,
#        /* array index */       0, 0,
#        /* port index */        0, 0,
#        /* register fields */   DIGITAL_INTERFACE_SELECT_RTL9607C_FIELDS,
#    },

/^#if defined\(CONFIG_SDK_CHIP_FEATURE/ {
    feature_name = gensub(/^.+FEATURE_([0-9A-Z_]+)\)$/, "\\1", "g");
    feature_name = gensub(/[_]+/, "_", "g", feature_name)
}

/register name/ {
    register_name = gensub(/^.*register name.*\"([0-9A-Z_]+)\",$/, "\\1", "g")
}

/offset address/ {
    offset_hex = gensub(/^.+[[:space:]]+0x([0-9A-F]+),$/, "\\1", "g");
}

/field numbers/ {
     field_numbers = gensub(/^.+[[:space:]]+([0-9]+),$/, "\\1", "g");
}

/array offset/ {
    array_offset = gensub(/^.+[[:space:]]+([0-9]+),$/, "\\1", "g");
}

/array index/ {
    array_index_lo =  gensub(/^.+[[:space:]]+([0-9]+),[[:space:]]+([0-9]+),$/, "\\1", "g");
    array_index_hi =  gensub(/^.+[[:space:]]+([0-9]+),[[:space:]]+([0-9]+),$/, "\\2", "g");
}

/port index/ {
    port_index_lo = gensub(/^.+[[:space:]]+([0-9]+),[[:space:]]+([0-9]+),$/, "\\1", "g");
    port_index_hi =  gensub(/^.+[[:space:]]+([0-9]+),[[:space:]]+([0-9]+),$/, "\\2", "g");
}

/register fields/ {
    print feature_name "," register_name ",0x" offset_hex "," field_numbers "," array_offset\
        "," array_index_lo "-" array_index_hi \
        "," port_index_lo "-" port_index_hi;
}
