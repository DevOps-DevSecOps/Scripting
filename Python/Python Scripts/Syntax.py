# """ How to write a comments in Python """ #

There are two types.

'Hash Symbol (#)'; it is an Single line comment.
a = 365
b = 7
#this is a comment
print(a%b) #find the remainder
#print(x//y)
#another comment

Docstrings Symbol (''' ''' or """ """) and it is an Multiline comment.
'''
print a word with an
exclamation mark following it.
'''


# """ How to clear Python Interpreter Console """ #
>>> import os                        # Check with Python Console
>>> clear = lambda:os.system('cls')
>>> clear()


# """ How to write a Standard Inputs """ #
>>> c = input('enter the value : ')  # Check with Python Console
enter the value : 70                 # Assigning a value to variable
>>> c                                # Checking the variable either value is assigned or not
70


# """ How to write Type in Python Interpreter Console """ #
>>> d = 101
>>> type(d)
<type 'int'>
