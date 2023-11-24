#!/bin/bash
distributions=("Ubuntu Fedora Manjaro Arch EndeavourOS Garuda")
for distro in $distributionsdo 
 if [[ "$distro" == "Arch" ]] ; 
   then 
   continue 
 fi 
 echo $distro
done
