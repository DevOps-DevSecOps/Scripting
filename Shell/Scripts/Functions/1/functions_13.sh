#!/bin/bash

function print(){
  local name=$1
  echo "the name is $name"
}

name="tom"

echo "the name is $name : Before"

print MAX

echo "the name is $name : After"
