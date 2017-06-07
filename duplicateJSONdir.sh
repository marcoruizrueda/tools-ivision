#!/bin/sh

#BASEDIR=`dirname "${0}"`/..
PATH_IMAGE_DIR=$1
PATH_JSON=$2

#echo "$PATH_IMAGE_DIR"
LIST_FILE=$(ls -d -1 "$PATH_IMAGE_DIR"*.*)
count=0

IFS='
'
for i in $LIST_FILE; do
#	readlink $i
	#echo "$i" | awk '{print $1$2$3}'
	count=$((count+1))
	echo $count $item
	echo "$i"
	./duplicateJSON.py -i "$i" -j "$PATH_JSON";
	
done

