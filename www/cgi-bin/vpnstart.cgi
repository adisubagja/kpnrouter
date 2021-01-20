#!/bin/sh

echo Content-type: text/html
echo

tunnel=`ls | grep \tmp\screenlog.0`
if [ -n "$tunnel" ]; then


echo kpn tunnel still injecting


else



echo "starting to inject pls wait" > \tmp\inject.log
printf 'y' | xderm start 

echo ktunnel has started

fi




