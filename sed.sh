#!/bin/bash
# bash test script only --RaymondS

#sed 's/^[[:digit:]]\{3\}/(&)/g' -e 's/[[:digit:]]\{3\}/&-/g' phone.txt
sed -e 's/^[0-9]\{3\}/(&)/g' -e 's/)[0-9]\{3\}/&-/g' phone.txt >>output.txt
echo '\n' >> output.txt

cat output.txt | sed 's/\(.*)\)\(.*-\)\(.*$\)/Area code: \1 Second: \2 Third: \3/'

rm output.txt