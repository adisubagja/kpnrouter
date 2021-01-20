#!/bin/sh


echo Content-type: text/plain
echo

awk 'NR==6' /www/payload.txt