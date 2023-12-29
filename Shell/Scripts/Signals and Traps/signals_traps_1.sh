trap "echo Exit signal is detected" SIGINT

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

$ ./signals_traps_1.sh
pid is 4703
1
2
Exit signal is detected                                                     # in another terminal executed an "kill -2 4703" command
3
4
5
6
7
^CExit signal is detected                                                   # ctrl+c is another signal
8
9
10

In another terminal execute the command to send the signal.
$ kill -2 4703

'
