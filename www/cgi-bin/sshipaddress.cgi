#!/bin/sh


echo Content-type: text/plain
echo
awk 'NR==1' /www/payload.txt