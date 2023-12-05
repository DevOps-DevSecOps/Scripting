#!/bin/bash
Str="Welcome to the fosslinux.com"
# Extracting string from index 15
echo ${Str:15} 
# Extracting string from index 15 of length 5
echo ${Str:15:5}

# ${string:position}
# ${string:position:length}
