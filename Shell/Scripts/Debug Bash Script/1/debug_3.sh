#!/bin/bash

set -x                                                                  # activate the debugging a bash script

file=/home/ec2-user/package-lock.json

set +x                                                                  # deactivate the debugging a bash script

trap "rm -vf $file && echo file deleted; exit" 0 2 15

echo "pid is $$"

while (( COUNT < 10 ))
do 
   sleep 10
   (( COUNT ++ ))
   echo $COUNT
done
exit 0

# MultipleLine Comments
: '

$ ./debug_3.sh

'
