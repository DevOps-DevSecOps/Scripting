#!/bin/bash

factorial() {
	
	if [ $1 -gt 1 ]; then
		echo $(( $1 * $(factorial $(( $1 -1 ))) ))
	else
		echo 1
	fi
	
}

echo -n "Factorial of $1 is: "
factorial $1
