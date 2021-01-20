#!/bin/sh


echo Content-type: text/plain
echo

awk 'NR==8' /www/payload.txt