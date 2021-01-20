#!/bin/sh



echo Content-type: text/html
echo
SET=`cat /www/cfg.sys`
echo "<select class='' name='config'>"
echo "<option>$SET</option>"
cd /www/ && ls *.mode | busybox sed 's/.mode//' | while read LINE; do
     echo "<option>$LINE</option>"
done
echo "</select>"
