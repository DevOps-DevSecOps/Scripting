#! /bin/bash

vehicle=$1

case $vehicle in
    "car" )
        echo "Rent of $vehicle is 100 dollar" ;;
    "van" )
        echo "Rent of $vehicle is 80 dollar" ;;
    "bicycle" )
        echo "Rent of $vehicle is 5 dollar" ;;
    "truck" )
        echo "Rent of $vehicle is 150 dollar" ;;
    * )
        echo "Unknown vehicle" ;;
esac

# MultipleLine Comments
: '

$ ./case_1.sh
Unknown vehicle

$ ./case_1.sh car
Rent of car is 100 dollar

$ ./case_1.sh  truck
Rent of truck is 150 dollar

'
