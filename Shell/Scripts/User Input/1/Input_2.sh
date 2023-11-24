#!/bin/bash

read -p "Enter a number and hit \"Enter\" " user_number1;



read -p "Enter another number and hit \"Enter\" " user_number2;






printf "You entered: %d and %d\n" $user_number1 $user_number2



printf "Added together they make: %d\n" $(( user_number1 + user_number2))
