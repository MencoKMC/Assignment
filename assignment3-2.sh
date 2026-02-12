#!/bin/bash
touch revenues.txt
curl -X POST "http://code001.ecsbdp.com/revenues?client=abc123" \
     -F "file=@revenues.txt"