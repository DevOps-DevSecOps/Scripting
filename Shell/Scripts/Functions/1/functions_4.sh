#!/bin/bash

arg() {
	echo "1st argument to function is $1 and 2nd is $2"
}

echo "1st argument to script is $1 and 2nd is $2"
arg $2 $1
