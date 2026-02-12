#!/bin/bash\
tail -n +2 countries.csv | cut -d',' -f1 | while read iso; do
    result=$(curl -s -D - "http://code001.ecsbdp.com/countries/$iso" -o /dev/null \
        | grep -o 'X-Code_Flag: FLAG{[^}]\+}' \
        | cut -d' ' -f2)
    if [ ! -z "$result" ]; then
        echo "FOUND in $iso: $result"
        break
    fi
done