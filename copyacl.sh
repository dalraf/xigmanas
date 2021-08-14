#/bin/bash
DIR1=$1
DIR2=$2

getfacl -q $DIR1 > /tmp/acltmp
setfacl -M /tmp/acltmp $DIR2 

rm /tmp/acltmp

getfacl $DIR1
getfacl $DIR2