#!/bin/sh


echo Content-type: text/plain
echo

awk 'NR==7' /www/payload.txt