#!/bin/bash

printf "This script is called: %s\n" $0



printf "You used %d command line parameters\n" $#



# loop through the variables



for param in "$@"; do



echo "$param"



done



echo "Parameter 2 was:" $2
