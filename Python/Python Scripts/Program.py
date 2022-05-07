#1st program#
login = {'Rollno':1234, 'Name':'aruntheja'}
subject = {'Hindi':70, 'English':90, 'Maths':99}

def result():
	if (login['Rollno'] == x) and (login['Name'] == y):
		print('Authentication Successful')

		print("Hindi: ", subject['Hindi'])
		print("English: ", subject['English'])
		print("Maths: ", subject['Maths'])

	else:
		print('Authentication Failed')

x = input('Enter Rollno: ')
y = input('Enter Name: ')

result()

print('@NEXT!#' * 10)


#2nd program#
login = {'Username':'aruntheja', 'Password':1994}

def access(a,b):
	if login['Username'] == x:
	 	print("Username Matched")

		if login['Password'] == y:
			print("Password Matched")
		else:
			print("Not Matched")

	else:
	    print("Username Not Matched")

x = input("Enter Username: ")
y = input("Enter Password: ")

access(x,y)

print('@NEXT!#' * 10)


#3rd program#
login = {'Rollno':1234, 'Name':'aruntheja'}
subject = {'Hindi':70, 'Maths':99, 'English':90}

def result():
	x = input("Enter rollno: ")
	y = input("Enter name: ")

	if (login['Rollno'] == x) and (login['Name'] == y):
		print("VERIFIED")

		print("Hindi: " + str(subject['Hindi']))
		print("Maths: " + str(subject['Maths']))
		print("English: " + str(subject['English']))
	
	else:
		print("NOT VERIFIED")
		
		result()          
					#keep going on up to the statement correct, Once it verified the execution will stop
result()

print('@NEXT!#' * 10)


#4th program#
login = {'Rollno':1234, 'Name':'arun'}
subject = {'Hindi':70, 'Maths':99, 'English':99}

count = 1

def result():
  global count
  x = input("Enter rollno: ")
  y = input("Enter name: ")

  if (login['Rollno'] == x) and (login['Name'] == y):
    print("VERIFIED")

    print("Hindi: " + str(subject['Hindi']))
    print("Maths: " + str(subject['Maths']))
    print("English: " + str(subject['English']))

  else:
    print("NOT VERIFIED")
    
    if count < 3:
      print(count)
      count+=1
      result()
    else:
      exit
      
result()

print('@NEXT!#' * 10)


#5th program#
login = {'Rollno':123, 'Name':'arun'}
subject = {'Hindi':70, 'Maths':82, 'English':99}

def result():
	x = input("Enter rollno: ")
	y = input("Enter name: ")
	
	if (login['Rollno'] == x) and (login['Name'] == y):
		print("VERIFIED")

		print("Hindi: " + str(subject['Hindi']))
		print("Maths: " + str(subject['Maths']))
		print("English: " + str(subject['English']))
	
	else:
	    print("NOT VERIFIED")
	    raise
try:
	result()
except:
	try:
		result()
	except:
		try:
			result()
		except:
		    print("BYE....BYE")

print('@NEXT!#' * 10)


#6th program#
def inp(number):
	x = input("Enter a no: ")
	y = input("Enter another no: ")

	if number == 1:
	    print(add(x,y))
	elif number == 2:
	    print(sub(x,y))
	elif number == 3:
	    print(mul(x,y)) 
	elif number == 4:
	    print(div(x,y))
	else:
	    print("NO operations")
def add(x,y):
    return(x+y)
def sub(x,y):
    return(x-y)
def mul(x,y):
    return(x*y)
def div(x,y):
    return(x/y)
while True:
    a = int(input("Enter \n 0:exit \n 1:add \n 2:sub \n 3:mul \n 4:div \n"))
    if a == 0:
              break
    inp(a)

print('@NEXT!#' * 10)


#7th program#
num1 = int(input('Enter your first number: '))
num2 = int(input('Enter your second number: '))
# Addition
print('{} + {} = '.format(num1, num2))
print(num1 + num2)
# Subtraction
print('{} - {} = '.format(num1, num2))
print(num1 - num2)
# Multiplication
print('{} * {} = '.format(num1, num2))
print(num1 * num2)
# Division
print('{} / {} = '.format(num1, num2))
print(num1 / num2)
