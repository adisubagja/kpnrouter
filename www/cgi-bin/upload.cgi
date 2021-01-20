#!/bin/ash






echo Content-type: text/html
echo


case "$REQUEST_METHOD" in
  POST)
    (


        cat $FILE | busybox sed -n '4p;8p;12p;16p;20p;24p;28p;32p;36p;40p' | busybox sed 's/\r$//' > /www/payload.txt
    )

    echo
    ;;

  *)
    echo

esac

ipadd=`awk 'NR==1' /www/payload.txt`
port=`awk 'NR==2' /www/payload.txt`
user=`awk 'NR==3' /www/payload.txt`
pass=`awk 'NR==4' /www/payload.txt`
squid=`awk 'NR==5' /www/payload.txt`
squidport=`awk 'NR==6' /www/payload.txt`
sni=`awk 'NR==7' /www/payload.txt`
portssl=`awk 'NR==8' /www/payload.txt`
payload=`awk 'NR==9' /www/payload.txt`

echo "$user
$pass
$port
$ipadd
" > /usr/bin/assh/akun.txt

echo "mode '1'
payload '$payload'
sni '$sni'
ip '$ipadd:$portssl'
proxy '$squid'
port '$squidport'
" > /usr/bin/assh/profile.txt








cat << EOF



<HTML>

<meta http-equiv="Refresh" content="0; url=http://192.168.1.1/index.html">

</HTML>



