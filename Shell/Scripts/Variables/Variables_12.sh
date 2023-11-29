#!/bin/bash

num1=50
num2=6

result=$(echo "$num1/$num2" | bc -l)

echo "The result is $result"
