#!/bin/bash

read -p "Enter the number: " num

mod=$(($num%2))

if [ $mod -eq 0 ]; then
	echo "Number $num is even"
else
	echo "Number $num is odd"
fi
