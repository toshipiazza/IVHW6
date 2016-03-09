#!/bin/bash
a=""
b=""
for i in $(seq 1 200)
do
    b=$(git diff --shortstat $(git rev-list -n1 --before="$i month ago" master))
    if [[ "$b" != "$a" ]]; then
        echo $i "month ago" $b
    fi
    a=$b
done
