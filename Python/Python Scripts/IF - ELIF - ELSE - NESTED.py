# """ IF - condition always look for True. """ #

if 100 < 10:
    print("100 is greater than 10")
print("good to see u")

a = 5
if a == 5:
    print("5 is equal to 10")
print('finished')

if 5 != 10:
    print("5 is not equal to 10")

if 10 <= 2:
    print("10 less than to 2")


# """ ELIF- If condition is not True and ELIF condition also look for True. """ #

if 5 == 10:
    print("5 is equal to 10")
elif 5 < 10:
    print("5 is less than 10")
else:
    print("5 is not equal and not less than 10")

b = 25
if b == 30:
    print('Equal')
elif 30 < b:
    print('less')
elif 30 > b:
    print('greater')
elif b != 35:
    print('not equal')
    

# """ ELSE - incase IF and ELIF conditions are not True. Then ELSE condition always look for False. """ #

c = 'aruntheja'
if c == 'arun':
    print("arun is equal to arun")
else:
    print("aruntheja is not equal to arun")


# """ NESTED """ #

d = 100
if d == 10:
    print(1*1)
else:
    if d != 1000:
        print(2*2)
    else:
        print(3*3)

e = 2
f = 4
if e == 1:
    print('HI')
elif (e == 2):
    print('NO HI')
    if 4 == f:
        print("Hello")
    else:
        print("No Hello")
g = 11
h = 22
i = 33
if 10 == g:
    print('Hello')
elif (i == 3):
    print('Good')
    if g == 12:
        print('Fine')
else:
    if h == 22:
        print('equal to')
    else:
        print('not equal to')


# """ ExampleS """ #

j = 2
k = 4
l = j * k
if l > 10:
    print('hmhm')
else:
    print('haha')

if not 4 == 50:        #Here Not(False)=True
    print('@@@@@@@')
else:
    print('#######')

if not 100 == 100:     #Here Not(True)=False
    print('ATK....')
else:
    print('atk....')

value = 111
if value > 111:
    print('bigger')
if value < 10:
    print('smaller')
else:
    print('none')

if 40 == 1:
    print('40 equal to 1')
elif 40 < 2:
    print('40 less than 2')
elif 40 > 20:
    print('40 greater than 20')
else:
    print('bye')

if 11 < 2:
    print('11 less than 2')
if 11 > 9:
    print('11 grater than 9')               #Here True
elif 11 <= 4:
    print('11 less than equal to 4')
elif 11 >= 11:
    print('11 greater than equal to 11')    #Here True
else:
    print('End')

m = 'xyz'
n = 'uvw'
if m != 'xyz':
    print('xyz')
elif n == 'uvw':
    print('uvw')
else:
    print('Nope')

o = 20
if 0 < o:
    if o < 40:
        print('Yes')
else:
    print('No')

if 0 < 20 and 20 < 40:
    print('PK')
else:
    print('MB')

if 0 < 20 < 40:
    print('Animals')
else:
    print('No Animals')

if (0 == 1) or (44 == 44):
    print('THOR')
else:
    print('thor')

name = 'ARUNTHEJAKUMAR'
DOB  = 1994
if name == 'tomcruise':
    print("Hero")
else:
    if 50 < 1994:
        print('HULK')
    else:
        print('hulk')

if 12 < 10:
    print('High')
else:
    print('Low')
    if 'ATK' == 'ATK':
        print('CAPTAIN AMERICA')
    else:
        print('captain america')
