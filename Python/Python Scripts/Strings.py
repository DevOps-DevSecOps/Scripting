# """ STRINGS - It is Immutable, once the string will be created the value can't be change the elements. """ #

# LENGTH - to find no of characters in string. #
length1 = "arun"
print(len(length1 + " " + "world"))

length2 = "Arun Theja"
length3 = len(length2)
print(length3)

length4 = "ArunTheja"
print(len(length4))


# CONCATENATION - join string together (or) combining strings. #
con1 = "Arun" + " " + "Theja"
print(con1)

con2 = "Arun " + "Kumar"
print(con2)

con3 = "arun" + " theja"
print(con3)

con4 = "EthAn" + "hUNt"
print(con4)

con5 = "tom "
con6 = "cruise"
print(con5 + con6)

con7 = "JACK"
con8 = " REACHER"
con9 = con7 + con8
print(con9)

con10 = "Mission"
print(con10 + ' Impossible')

con11 = "NYC"
con12 = "SHOW"
print('welcome to ' + con11 + ' and enjoy the ' + con12)
print('welcome to %s and enjoy the %s' %(con12, con11))
print('welcome to %s' %con11)


# MULTIPLYING #
mul1 = 'ARUN'
mul2 = 'theja'
print(mul1 * 3 + mul2)

mul3 = 'arun'
mul4 = ' Theja'
mul5 = mul3 * 3 + mul4
print(mul5)

print("The " * 3 + "Mummy")

mul6 = 'nageswara '
mul7 = 'rao'
print(2 * mul6 + mul7)

mul8 = 'Thank ' * 5
print(mul8 + 'YOU')

mul9 = '1994 ' * 4
print(mul9)


# APPEND #
append1 = 'mahesh'
append1 += ' '
append1 += 'babu'
print(append1)

append2 = 'super'
append2 += ' '
append2 += 'star'
print(append2)


# LOWER #
lower1 = "MUNI LAKSHMI"
lower1 = lower1.lower()
print(lower1)

print('speed'.islower())


# UPPER #
upper1 = "power star"
print(upper1.upper())
print(upper1.isupper())

print('STAR'.isupper())


# COUNTS #
count1 = "That THAT An Is noT bad so that an iS noT it an"
print(count1.count("t")) 

count2 = "That THAT An Is noT bad so that an iS noT it an"
count2 = count2.lower()
print(count2.count("t"))

count3 = "daddy"
print(count3.count('d'))


# COUNTER #
from collections import Counter

counter1 = [1, 1, 1, 1, 15, 2, 2, 3, 3, 3, 3, 5, 5, 5]
print(Counter(counter1))

counter2 = 'arunthejakumartomcruisemaheshbabu'
print(Counter(counter2))

counter3 = 'Hi boss does boss Hi up Hi does the boss'
print(Counter(counter3.split()))

counter4 = ['The', 'place', 'have', 'The', 'place', 'The', 'man', 'The']
counter5 = Counter(counter4)
print(counter5.most_common(2))


# CONVERSION #
convert1 = 'HI'
convert2 = 2.0
print(convert1 + str(convert2))


# CAPITALIZE #
capitalize1 = 'abcd efgh'
print(capitalize1.capitalize())


# ESCAPE - in between of sentence one more string will be there by using backslash (\) it will escape the string in between sentence. #
escape = "I am a single quoted string don\"t"
print(escape)

print("i am \"Arun Theja\"")

print("i am \\ArunTheja")       #Backslsh print in program

print("i'm ARUNTHEJA")

print("Need to use quotes inside \
a string")

print(' "this is quote" ')

print("Hi \t Hello \n bye")     #\t - tab space, \n - new line


# REPLACE a string #
replace1 = "ARUN THEJA"
replace1 = replace1.replace("T", 't')
print(replace1)

replace2 = "TOM CRUISE"
replace2 = replace2.replace("TOM CRUISE", 'Tom Cruise')
print(replace2)

replace3 = "1abc 2abc 3abc 4abc"
replace3 = replace3.replace('abc', "ABC")
print(replace3)

'''string replace maximum counts '''
replace4 = "this is my first program, it is very easy is" 
replace4 = replace4.replace("is", 'WAS', 4)  
print(replace4)

replace5 = "this is an my first is last"
replace5 = replace5.replace("is", 'AN', 2)
print(replace5)

replace6 = "1abc 2abc 3abc 4abc"
replace6 = replace6.replace('abc', "ABC", 2)
print(replace6)


# STRIP - used for to remove spaces. #
strip1 = " I am ArunTheja "
strip1 = strip1.strip()
print(strip1)

print(" My good name is ATK ".strip())

strip2 = "Made In China"
print(strip2.replace(" ",''))       #strip replace will remove space in between sentence


# SPLIT - used seperate the words. #
split1 = "Welcome to my World"
print(split1.split())
print(split1.split(","))
print(split1.split(" "))
print(split1.split( ))
print(split1.split('to'))
print(split1.split('m'))


# FIND #
'''By using index method we can do the operation.
   H e l l o   W o r l d
   0 1 2 3 4 5 6 7 8 9 10'''

find1 = "Hello World"
find2 = find1.find("w")
find3 = find1.find("W")
print(find2)
print(find3)


# SLICING - if u want to slice off unwanted parts of a string from the beigning are end you can do so creating a substring or cutting in to peaces. #
'''By using index method.
    [start index : end index + 1]
   T  h i s   i s   M e s  s  a  g  e      -->character
   0  1 2 3 4 5 6 7 8 9 10 11 12 13 14     -->index  '''

slice1 = "This is Message"
print(slice1[:])
print(slice1[0:15])
print(slice1[0:7])
print(slice1[8:15])
print(slice1[5:])
print(slice1[:7])
print(slice1[4:9])
print(slice1[7:14])


# REVERSE SLICING - i have to use [::-1] it will reverse the string. #
'''By using index method.
    [start index : end index - 1]
   H  i   H o w   a r e    y  o  u      -->character
   0  1 2 3 4 5 6 7 8 9 10 11 12 13     -->index  '''

slice2 = "Hi How are You"
print(slice2[::-1])
print(slice2[7:0:-1])
print(slice2[13:7:-1])
print(slice2[9::-1])
print(slice2[:5:-1])
print(slice2[9:3:-1])
print(slice2[13:6:-1])
print(slice2[-1])
print(slice2[:-1])
print(slice2[::1])
print(slice2[::2])
print(slice2[::])


# STEPS #
steps1 = "abcdefghijklmnopqrstuvwxyz"
print(steps1[1:16:2])


# INDEX #
index1 = 'This is my world'
print(index1[2])
print(index1[12])

index2 = 'nyc' [2]
print(index2)

index3 = "arun", "theja", "kumar"
print(index3[1][3])


# PRINT FORMATING #
format1 = 'string'
print('place my variable here:%s' %(format1))

print('Floating point number:%1.1f' %(13.145))
print('Floating point number:%1.2f' %(13.145))
print('Floating point number:%1.10f' %(13.145))
print('Floating point number:%25.3f' %(13.145))

print('First:%s, Second:%s, Thrid:%s' %('hi!', 'two', 3))
print('First:{x} Second:{x}'.format(x = 'inserted', y = 'two!'))
print('First:{x} Second:{y} Thrid:{x}'.format(x = 'inserted', y = 'two!'))

format2 = "arun theja kumar"
print('Say HI to: ', format2)

format3 = "TOM CRUISE"
print('Say HI to: ' + format3)

format4 = "Jack Reacher"
print('Say HI to: ' + str(format4))


# STRING FORMATING #
a = 10
b = 20
c = 30
D = "aRuN"
E = "ThEjA"
F = "KumAr"
                                                
print("Less value = {0}, Greater value = {1}".format(a, b))  #(a,b) - character; (0,1) - index
print("Less value = {1}, Greater value = {0}".format(a, b))
print("Less value = {0}, Greater value = {0}".format(a, b))
print("{0}".format(c,a))                                    #(c,a) - character; (0,1) - index
print("fullname = {0}{1}".format(D, E))
print("BYE = {2}.....,HI = {0}.....,HELLO = {1}".format(D, E, F))
print("BYE = {2}.....,HI = {0}.....,HELLO = {1}".format(F, D, E)) #(F, D, E) - character; (0,1,2) - index

print("num1 = {0}, num2 = {1}, num3 = {2}".format(11, 22, 33))    #(11, 22, 33) - (0,1,2)
print("Value1 = {a}, Value2 = {b}, Value3 = {c}".format(a=44, b=55, c=66))
print("Count1 = {d}, Count2 = {0}".format(123, 456, d='ATK'))
print("My name is {name}, and age is {0}".format(24, name='TOMCRUISE'))
print('{:>30}'.format("ArunThejaKumar"))
print('{:<30}'.format("JackReacher", "MissionImpossible"))
print('{:b}'.format(21))                #Binary Decimal Value


# CENTER #
center1 = "MummY"
center1 = center1.center(15, 'A')
print(center1)
