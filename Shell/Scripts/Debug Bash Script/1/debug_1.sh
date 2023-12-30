#!/bin/bash

file=/home/ec2-user/package-lock.json

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

debugging a bash script using a command.
$ bash -x ./debug_1.sh

'
