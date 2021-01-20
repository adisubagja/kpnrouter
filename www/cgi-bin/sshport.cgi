#!/bin/sh


echo Content-type: text/plain
echo

awk 'NR==2' /www/payload.txt