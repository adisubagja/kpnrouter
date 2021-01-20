#!/bin/sh
echo Content-type: text/html
echo
log1=`cat /tmp/screenlog.0 `
log2=`cat /tmp/inject.log `

echo " $log1$log2" > /tmp/log.txt
cat /tmp/log.txt
