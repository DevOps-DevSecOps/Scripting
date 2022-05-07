# """ FOR - it is usually characterized by the use of an implicit or explicit iterator. In each iterator step a loop variable is set to a value in a sequence or other data collection. This kind of for loop is known in most unix and linux shell and it is the one which is implemented in python. We can use ranges in for loop. """ #

#1st program#
for for1 in range(11):
    print(for1)

#2nd program#
for2 = ['arun', 32, 5.6]
for for3 in for2:
    print(for3)

#3rd program#
for for4 in range(3, 12):
    print(for4)

#4th program#
for for5 in range(1, 11, 2):
    print(for5)

#5th program#
for for6 in range(2, 20, 3):
    print(for6)

#6th program#
for7 = 'theja', 20, 6.6
for for8 in for7:
    print(for8)

#7th program#
for9 = [23, 45, 96]
for for10 in for9:
    print(for10)
else:
    print("No Values")

#8th program#
for11 = 'ATK'
for for12 in range(1, 3):
    print("Enter no = {0}, My name = {1}".format(for12, for11))

#9th program#
for13 = [1, 10, 100, 1000]
for for14 in for13:
    print("Enter no = {0}".format(for14))

#10th program#
for15 = ['arun', 'theja', 'kumar']
for for16 in for15:
    print("Enter a Value = {0}".format(for16))

#11th program#
for17 = 'abcde'
for for18 in for17:
    print(for18)

#12th program#
for19 = ['bmw', 'benz', 'honda']
for for20 in for19:
    print(for20)

#13th program#
for21 = [1, 2, 3]
for for22 in for21:
    print(for22 * 10)

#14th program#
for23 = {'one':1, 'two':2, 'three':3}
for for24 in for23:
    print(for24 + " " + str(for23[for24]))

#15th program#
for25 = {'one':1, 'two':2, 'three':3}
for A, B in for25.items():              #Here A is key, B is value
    print(A)
    print(B)

#16th program#
for26 = [1, 2, 3, 4]
for for27 in for26:
    print('HELLO')

#17th program#
for28 = [22, 33, 44]
for for29 in for28:
    if for29 % 2 == 1:
        print(for29)

#18th program#
for30 = [2, 4, 6, 8]
for31 = 0
for for32 in for30:
    for31 = for31 + for32
print(for31)

#19th program#
for33 = ['RED']
for for34 in for33:
    if for34 == "RED":
        for33 += ['Black']
    if for34 == "Black":
        for33 += ['white']
print(for33)

#20th program#
for35 = ['x', 'y', 'z']
for36 = 0
for for37 in for35:
    print(for36)
    print(for37)
    for36 += 1

#21st program#
for38 = [(23,41),(65,82),(10,34)]
for (C, D) in for38:
    print(C)

#22nd program#
for39 = (24, 36, 57)
for for40 in for39:
    print(for40)

#23rd program#
for41 = [(78,49),(85,94),(100,364)]
for for42 in for41:
    print(for42)

#24th program#
for43 = [100, 200, 300, 400]
for44 = 0
for for45 in for43:
    for44 = for44 + for45
    print(for44)


# """ WHILE - is repeatedly executes a target statement as long as a given condition is true. If loop will go continuously it is infinite loop. """ #

#1st program#
a = 0
while a < 5:
    print("TRUE")
    a = a + 1
''' 0<5(T), 0+1=1, 1<5(T), 1+1=2, 2<5(T), 2+1=3, 3<5(T), 3+1=4, 4<5(T), 4+1=5, 5<5(F) '''

#2nd program#
b = 0
while b < 5:
    b = b + 1
    print(b)

#3rd program#
c = 10
d = 20
e = 30
while e <= c:
    d = d + e
    e = e + 1
print(e)

#4th program#
f = 10
g = 20
h = 30
while h <= f:
    g = g + h
    h = h + 1
print(h, g)

#5th program#
i = 0
while i < 5:
    print(i, 'less')
    i = i + 1
else:
    print(i, 'not less')
''' 0<5, 0+1=1, 1<5, 1+1=2, 2<5, 2+1=3, 3<5, 3+1=4, 4<5, 4+1=5, 5<5 '''

#6th program#
j = [1, 2 , 3, 4]
k = 0
while k < len(j):
    print(j[k])
    k = k + 1
print("Bye")
''' [1, 2, 3, 4] = 4 elements
     0  1  2  3 --> index
     len(i) = 4 elements
     print(j[k]) = print(j[0]) ,here 0 is index 
     k = k + 1 = 0 + 1 = 1
     k = 1
     1 < 4
     print(i[1])
     k = 1 + 1 =2 '''

#7th program#
l = ['Hello', 'World', 'how', 'are', 'U']
m = 0
while m < len(l):
    print(l[m])
    print(len(l[m]))
    m = m + 1
    print("COMPLETED")
'''m < len(l)
   len(l) = 5 elements and m = 0
   0 < 5
   print(l[m]) = print(l[0])  ,here 0 is index
   m = m + 1 = 0 + 1 = 1
   m < len(l) - 1 < 5
   print(i[1])
   m = 1 + 1 = 2'''

#8th program#
n = 0
while n < 3:
    print("Inside Loop")
    n = n + 1
else:
    print("Inside Else")

#9th program#
o = 0
while o < 5:
    print(o)
    o = o + 1
print("See U")

#10th program#
p = 0
while p < 5:
    print('p is currently: ' + str(p))
    p += 1
else:
    print('All Done')

#11th program#
q = 0
while q < 5:
    print('Value of q is: ' + str(q))
    q += 1

#12th program#
r = []
s = 0
while s < 10:
    r.append(s)
    print("Value of s is: " + str(s))
    s += 1
print(r)

#13th program#
t = 2
while t < 7:
    print("Value of t is: " + str(t))
    t = t + 1
else:
    print("thank u")

#14th program#
u = 0
while u < 4:
    print("Value of u is: " + str(u))           #infinite loop


# """ NESTED - the placing of one loop inside the body of another loop is called nesting. When you nest two loop, the outer loop takes control of the no of complete repetitions of the inner loop. While all types of loop may be nested, teh most commonly nested loops are for loops. """ #

#1st program#
n = 5
for o in range(1, n):
    for p in range(1, n + 1):
        for q in range(1, p + 1):
            print(q)
print("ByE")

#2nd program#
r = 0
s = 0
while r < 4:
    r = r + 1
    while s < 4:
        s = s + 1
        print(r, s)
