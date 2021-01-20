#!/bin/sh

echo Content-type: text/html
echo
echo

FILE=`cat`
case "$REQUEST_METHOD" in
  POST)
    (
	     

		
	echo "$FILE" | busybox sed -n '4p' | busybox sed 's/\r$//' > /www/cfg.sys
SSLOCATE=`cat /www/cfg.sys`

mode=`cat /www/$SSLOCATE.mode`





sed -i "1s/.*/$mode/" /usr/bin/assh/profile.txt




    )


    echo
    ;;

  *)

    echo

esac







cat << EOF

<HTML>

<meta http-equiv="Refresh" content="0; url=http://192.168.1.1/index.html">

</HTML>




