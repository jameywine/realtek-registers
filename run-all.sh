#!/bin/bash

PLATFORMS="rtl9607c"


#
# main
#

BASE=$(dirname $0)

if [ $# != 1 ]; then
	echo "Usage: $0 <SDK directory>"
	exit 1
fi

chipdef=$1
if [ ! -d $chipdef ]; then
	echo "$chipdef not found, not the right SDK directory"
	exit 1
fi

echo "Parsing SDK source code"
for pl in $PLATFORMS; do
	path=$chipdef/$pl
	prefix=rtk_${pl}_
	echo "$pl..."
	awk -f $BASE/reglist.awk < $path/${prefix}reg_list.c > reglist-$pl.csv
	awk -f $BASE/regfieldlist.awk < $path/${prefix}regField_list.c > regfieldlist-$pl.csv
#	awk -f $BASE/tablelist.awk < $path/${prefix}table_list.c > tablelist-$pl.csv
#	awk -f $BASE/tablefieldlist.awk < $path/${prefix}tableField_list.c > tablefieldlist-$pl.csv
done

#if [ ! -e "realtek_reglist.py" ]; then
#	ln -s ../webapp/realtek_reglist.py .
#fi
#
echo "Generating registers"
python3 parse-csv-registers.py
#
#echo "Generating tables"
#python3 import-table-info.py
