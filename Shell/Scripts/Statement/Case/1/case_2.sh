#! /bin/bash

echo -e "Enter some character : \c"
read value

case $value in
    [a-z] )
        echo "User entered $value a to z" ;;
    [A-Z] )
        echo "User entered $value A to Z" ;;
    [0-9] )
        echo "User entered $value 0 to 9" ;;
    ? )
        echo "User entered $value Special Character" ;;
    * )
        echo "Unknown Input" ;;
esac

# MultipleLine Comments
: '

$ ./case_2.sh
Enter some character : f
User entered f a to z

$ ./case_2.sh
Enter some character : E
User entered E A to Z

$ ./case_2.sh
Enter some character : 5
User entered 5 0 to 9

$ ./case_2.sh
Enter some character : &
User entered & Special Character

$ ./case_2.sh
Enter some character : aB1&
Unknown Input
'
