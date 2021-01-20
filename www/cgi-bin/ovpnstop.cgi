#!/bin/sh

echo Content-type: text/html
echo

tunnel=`ls | grep \tmp\screenlog.0`
if [ -n "$tunnel" ]; then

echo ktunnel has already stopped

else

killall redsocks
printf 'y' | xderm stop 
cd /tmp/
rm screenlog.0
rm inject.log
cd ..


echo ktunnel has stop

fi
