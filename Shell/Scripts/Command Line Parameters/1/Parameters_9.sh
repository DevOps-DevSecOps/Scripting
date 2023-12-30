#! /bin/bash

echo $1 $2 $3 ' > echo $1 $2 $3 '

echo $0 $1 $2 $3 ' > echo $1 $2 $3 '

args=("$@")

echo ${args[0]} ${args[1]} ${args[2]} ${args[3]}

echo "#---* Special Variables *---#"

echo $@

# print the number of arguments passed to script.
echo $#                                          



# MultipleLine Comments
: '

$ ./Parameters_9.sh Mark Tom John
Mark Tom John  > echo $1 $2 $3 
./Parameters_9.sh Mark Tom John  > echo $1 $2 $3 
Mark Tom John
#---* Special Variables *---#
Mark Tom John
3

'
