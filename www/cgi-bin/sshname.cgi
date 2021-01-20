#!/bin/sh


echo Content-type: text/plain
echo
awk 'NR==3' /www/payload.txt