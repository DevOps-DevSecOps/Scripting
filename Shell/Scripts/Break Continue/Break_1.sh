#!/bin/bash
distributions=("Ubuntu Fedora Manjaro Arch EndeavourOS Garuda")
for distro in $distributions
do 
 if [[ "$distro" == "Arch" ]] ; 
   then 
   break 
 fi 
 echo $distro
done
