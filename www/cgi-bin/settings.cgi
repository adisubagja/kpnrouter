#!/bin/sh




case "$REQUEST_METHOD" in
  POST)
    (

       cat $FILE | busybox sed -n '4p' | busybox sed 's/\r$//' > /www/setttings.txt

    )

    echo
    ;;

  *)
    echo

esac

ipadd=`awk 'NR==2' /www/setttings.txt`
squidport=`awk 'NR==7' /www/setttings.txt`
user=`awk 'NR==4' /www/setttings.txt`
pass=`awk 'NR==5' /www/setttings.txt`
sni=`awk 'NR==6' /www/setttings.txt`
portssl=`awk 'NR==7' /www/setttings.txt`
port=`awk 'NR==3' /www/setttings.txt`







cat << EOF



<HTML>

<meta http-equiv="Refresh" content="0; url=http://192.168.1.1/index.html">

</HTML>



