#!/bin/sh


echo Content-type: text/plain
echo

awk 'NR==10' /www/payload.txt