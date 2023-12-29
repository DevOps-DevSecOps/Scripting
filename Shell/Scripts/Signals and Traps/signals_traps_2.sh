trap "echo Exit signal is detected" SIGKILL

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

$ ./signals_traps_2.sh
pid is 10044
1
2
3
4
5
Killed

In another terminal execute the command to send the signal.
$ kill -SIGKILL 10044

'
