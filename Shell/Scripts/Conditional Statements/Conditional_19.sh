#! /bin/bash

count=10

if [ $count -eq 10 ]
then
  echo "condition is true"
fi

if [ $count -ne 9 ]
then
  echo "condition is true"
fi



count_0=10

if [ $count_0 -gt 9 ]
then
  echo "condition is true"
fi

if [ $count_0 > 9 ]
then
  echo "condition is true"
fi



count_1=10

if [ $count_1 > 9 ]
then
  echo "condition is true"
fi

if (( $count_1 > 9 ))
then
  echo "condition is true"
fi

if (( $count_1 >= 9 ))
then
  echo "condition is true"
fi



word=abc

if [ $word = "abc" ]
then
  echo "condition is true"
fi

if [ $word != "abc" ]
then
  echo "condition is true"
fi



words=a 

if [[ $words < "b" ]]
then
  echo "condition is true"
fi

if [[ $words == "b" ]]
then
  echo "condition is true"
else
  echo "condition is false"
fi

if [[ $words == "b" ]]
then
  echo "condition b is true"
elif [[ $words == "a" ]]
then
  echo "condition a is true"
else
  echo "condition is false"
fi
