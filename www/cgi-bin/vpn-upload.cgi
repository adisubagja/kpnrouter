#!/bin/ash






echo Content-type: text/html
echo


case "$REQUEST_METHOD" in
  POST)
    (


        cat $FILE | busybox sed -n '4p;8p;12p;16p;20p;24p;28p;32p;36p;40p' | busybox sed 's/\r$//' > /etc/openvpn/account.txt
    )

    echo
    ;;

  *)
    echo

esac






cat << EOF



<HTML>

<meta http-equiv="Refresh" content="0; url=http://192.168.1.1/vpn.html">

</HTML>



