#!/bin/bash

function print(){
  echo $1
}

quit () {
  exit
}

print Hello
print World
print Again

echo "DonE"

quit
