#if defined(CONFIG_SDK_CHIP_FEATURE_INTERFACE)
#if defined(CONFIG_SDK_RTL9607C)
#rtk_regField_t DIGITAL_INTERFACE_SELECT_RTL9607C_FIELDS[] =
#{
#    {   /* name */          RTL9607C_RESERVEDf,
#        /* lsp */           2,
#        /* len */           30,
#        #if defined(CONFIG_SDK_DUMP_REG_WITH_NAME)
#        /* field name */    "RESERVED",
#        #endif  /* CONFIG_SDK_DUMP_REG_WITH_NAME */
#    },
#    {   /* name */          RTL9607C_ORG_COLf,
#        /* lsp */           1,
#        /* len */           1,
#        #if defined(CONFIG_SDK_DUMP_REG_WITH_NAME)
#        /* field name */    "ORG_COL",
#        #endif  /* CONFIG_SDK_DUMP_REG_WITH_NAME */
#    },
#    {   /* name */          RTL9607C_ORG_CRSf,
#        /* lsp */           0,
#        /* len */           1,
#        #if defined(CONFIG_SDK_DUMP_REG_WITH_NAME)
#        /* field name */    "ORG_CRS",
#        #endif  /* CONFIG_SDK_DUMP_REG_WITH_NAME */
#    },
#};

/^#if defined\(CONFIG_SDK_CHIP_FEATURE/ {
    feature_name = gensub(/^.+FEATURE_([0-9A-Z_]+)\)$/, "\\1", "g");
    feature_name = gensub(/[_]+/, "_", "g", feature_name)
}

/rtk_regField_t/ {
    reg_name = gensub(/^[^ ]+ ([0-9A-Z_]+)_.*_FIELDS\[\] =$/, "\\1", "g");
}

/\/\* name \*\//{
    field_name = gensub(/^[^\n]*[[:space:]]+[^_]*_([0-9A-Z_]+)f,$/, "\\1", "g");
}

/\/\* lsp \*\//{
    field_lsb = gensub(/^.+[[:space:]]+([0-9A-F]+),$/, "\\1", "g");
}

/\/\* len \*\//{
    field_len = gensub(/^.+[[:space:]]+([0-9A-F]+),$/, "\\1", "g");
    print feature_name "," reg_name "," field_name "," field_lsb "," field_len
}
