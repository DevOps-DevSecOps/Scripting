#!/bin/bash

echo "Table for $1 is:"
index=1
while [ $index -le 10 ]; do
	echo $(($1*$index))
	index=$(($index+1))
done
