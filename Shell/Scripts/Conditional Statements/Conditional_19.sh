#! /bin/bash

echo "**---ONE---**"

count=10

if [ $count -eq 10 ]
then
  echo "condition is true"
fi

if [ $count -ne 9 ]
then
  echo "condition is true"
fi

echo "**---TWO---**"

count_0=10

if [ $count_0 -gt 9 ]
then
  echo "condition is true"
fi

if [ $count_0 > 9 ]
then
  echo "condition is true"
fi

echo "**---THREE---**"

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

echo "**---FOUR---**"

word=abc

if [ $word = "abc" ]
then
  echo "condition is true"
fi

if [ $word != "abc" ]
then
  echo "condition is true"
fi

echo "**---FIVE---**"

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
