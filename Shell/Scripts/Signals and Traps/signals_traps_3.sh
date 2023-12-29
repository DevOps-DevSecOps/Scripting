#!/bin/bash

file=/home/ec2-user/package-lock.json

trap "rm -f $file; exit" 0 2 15

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

execute the script, without sending a signal.
$ ./signals_traps_3.sh
pid is 19333
1
2
3
4
5
6
7
8
9
10

list the file is available.
$ ls /home/ec2-user/
package-lock.json

execute the script, with sending a signal from another terminal.
$ ./signals_traps_3.sh
pid is 19479
1
2
3

In another terminal execute the command to send the signal.
$ kill -2 19479
$ kill -15 19479

again list the file and now it will be deleted.
$ ls /home/ec2-user/

'
