#!/bin/sh


echo Content-type: text/plain
echo
awk 'NR==4' /www/payload.txt