#!/bin/bash
a=""
b=""
for i in $(seq 0 200)
do
    b=$(git diff --stat $(git rev-list -n1 --before="$i month ago" master))
    if [[ "$b" != "$a" ]]; then
        echo $i "month ago" $b
    fi
    a=$b
done
