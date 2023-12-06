#!/bin/bash

sum() {
	sum=$(($1+$2))
	echo "The sum of $1 and $2 is: $sum"
}

echo "Let's use the sum function"
sum 1 5
