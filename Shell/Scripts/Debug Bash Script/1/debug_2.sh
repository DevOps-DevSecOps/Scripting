#!/bin/bash -x                                                      

# -x debugging a bash script

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

$ ./debug_2.sh

'
