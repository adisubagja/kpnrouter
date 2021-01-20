#!/bin/sh


echo Content-type: text/plain
echo
awk 'NR==9' /www/payload.txt