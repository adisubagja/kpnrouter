#!/bin/sh

echo Content-type: text/html
echo
echo

FILE=`cat`
case "$REQUEST_METHOD" in
  POST)
    (
	
       

		echo "$FILE" | busybox sed -n '4p' | busybox sed 's/\r$//' > /www/vpn/cfg.sys
		
LOCATE=`cat /www/vpn/cfg.sys`

LPORT=`cat /www/vpn/$LOCATE.ovpn | grep "remote " | busybox awk '{print $2}'`

	
		cat /www/vpn/$LOCATE.ovpn > /etc/openvpn/server.ovpn



sed -i 's/auth-user-pass/ /g' /etc/openvpn/server.ovpn
echo "auth-user-pass /etc/openvpn/account.txt " >> /etc/openvpn/server.ovpn
echo "log /tmp/openvpn.log " >> /etc/openvpn/server.ovpn
 



    )


    echo
    ;;

  *)

    echo

esac





/etc/init.d/openvpn stop
rm /tmp/openvpn.log



cat << EOF

<HTML>

<meta http-equiv="Refresh" content="0; url=http://192.168.1.1/vpn.html">

</HTML>




