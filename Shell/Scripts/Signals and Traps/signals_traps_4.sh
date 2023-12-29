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

list the file is available.
$ ls /home/ec2-user/
package-lock.json

execute the script, without sending a signal.
$ ./signals_traps_4.sh
pid is 22719
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
removed '/home/ec2-user/package-lock.json'
file deleted

again list the file and now it will be deleted.
$ ls /home/ec2-user/

again recreate and list the file is available.
$ touch /home/ec2-user/package-lock.json

again list the file is available.
$ ls /home/ec2-user/
package-lock.json

execute the script, with sending a signal from another terminal.
$ ./signals_traps_4.sh
pid is 23018
1
2
3
4
5
removed '/home/ec2-user/package-lock.json'
file deleted
file deleted

In another terminal execute the command to send the signal.
$ kill -2 23018
$ kill -15 23018

again list the file and now it will be deleted.
$ ls /home/ec2-user/

'
