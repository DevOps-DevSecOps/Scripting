#! /bin/bash

echo "please enter your username"
read NAME                                                 # it takes input from above and assigns it as the value of the variable NAME

if [ "$NAME" = "Elliot" ];
then
  echo "welcome back Elliot"
else
  echo "Invalid Username"
fi
