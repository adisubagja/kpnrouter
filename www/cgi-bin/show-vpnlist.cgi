#!/bin/sh



echo Content-type: text/html
echo
SET=`cat /www/vpn/cfg.sys`
echo "<select class='y' name='config-vpn'>"
echo "<option>$SET</option>"
cd /www/vpn/ && ls *.ovpn | busybox sed 's/.ovpn//' | while read LINE; do
     echo "<option>$LINE</option>"
done
echo "</select>"
