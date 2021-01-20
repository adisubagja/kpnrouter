#!/bin/sh


echo Content-type: text/plain
echo

awk 'NR==5' /www/payload.txt