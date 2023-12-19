#! /bin/bash

read -p 'username : ' user_var
read -sp 'password : ' pass_var
echo
echo "username : $user_var"
echo "password : $pass_var"

# MultipleLine Comments
: '
Here password input doesnot visible while giving in CLI.
$ ./Input_14.sh
username : myuser
password : 
username : myuser
password : 12345
'
