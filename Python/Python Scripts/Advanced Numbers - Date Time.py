#""" ADVANCED NUMBERS - It is Immutable. """ #

a = hex(12)
print(a)

b = hex(512)
print(b)

c = bin(1234)
print(c)

d = pow(2,4)
print(d)

e = abs(2)
print(e)

f = abs(-3)
print(f)

g = round(3.9)
print(g)

h = round(3.141592,2)
print(h)


# """ DATE and TIME """ #

import datetime

Time = datetime.time(5,25,1)
print(Time)
print(Time.minute)
print(datetime.time.min)
print(datetime.time.max)
print(datetime.time.resolution)

Today = datetime.date.today()
print(Today)
print(Today.timetuple())
print(Today.day)
print(datetime.date.min)
print(datetime.date.resolution)

D1 = datetime.date(2016,9,30)
D2 = D1.replace(year = 2017)
print(D1)
print(D2)
print(D1-D2)
