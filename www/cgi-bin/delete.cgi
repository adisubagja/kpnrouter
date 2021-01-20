#!/bin/sh
PRINT=`cat`
FILENAME=`echo "$PRINT" | busybox sed -n '4p' | busybox sed 's/\r$//'`
rm "/tmp/$FILENAME.ovpn"
SET=`cat /www/cfg.sys`

if [ "$SET" = "$FILENAME" ]; then 

rm "/www/cfg.sys"


fi

cat << EOF

<HTML>

<meta http-equiv="Refresh" content="0; url=http://192.168.1.1/index.html">

</HTML>