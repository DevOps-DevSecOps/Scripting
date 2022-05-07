# """ TYPE """ #

type1 = 5
type2 = 12.34
type3 = 'arunthejakumar'
type4 = True
print(type(type1))
print(type(type2))
print(type(type3)) 
print(type(type4))


# """ RANGE """ #

range1 = range(0, 10)
print(range1)

range2 = 4
range3 = 18
print(range(range2, range3))

range4 = 4
range5 = 18
print(range(range4, range5, 3))   #Here 3 is step

range6 = [1, 2, 3, 4, 5]
for range7 in range6:
    print(range7)

range8 = range(0, 10, 2)          #Here 2 is step
print(range8)

for range9 in xrange(2, 8):
    print(range9)

print(list(range(0, 5)))


# """ LIST COMPREHENSION """ #

lc1 = [letter for letter in 'word']
print(lc1)

lc2 = []
for lc3 in 'world':
    lc2.append(lc3)
print(lc3)

lc4 = [x**2 for x in range(0,11)]
print(lc4)

lc5 = [number for number in range(11) if number % 2 == 0]
print(lc5)

lc6 = []
for lc7 in range(11):
    if lc7 % 4 == 2:
        lc6.append(lc7)
print(lc6)

lc8 = [0, 10, 20.11, 34.5]
lc9 = [(x * (9/5.0) + 32) for x in lc8]
print(lc9)

lc10 = [x**2 for x in [x**2 for x in range(11)]]
print(lc10)

lc11 = [num for num in range(0,50) if num % 3 ==0]
print(lc11)

for lc12 in range(11):
    if lc12 % 5 == 0 and lc12 % 3 == 0:
        print('FizzBuzz')
    elif lc12 % 3 == 0:
        print('Fizz')
    elif lc12 % 5 == 0:
        print('Buzz')
    else:
        print(lc12)


# """ LAMBDA """ #

#1st program#
a = [1, 2, 3]           #Here m(0)-1, m(1)-2, m(2)-3
b = [4, 5, 6]           #Here k(0)-4, k(1)-5, k(2)-6
c = [7, 8, 9]           #Here l(0)-7, l(1)-8, k(2)-9
print(map(lambda d,e : d + e, a,b)) 

#2nd program#
f = [10, 11, 12]           
g = [13, 14, 15]           
h = [16, 17, 18]           
print(map(lambda i,j,k : i + j + k, f,g,h))

#3rd program#
l = [19, 20, 21]
print(map(lambda m : m * - 1, l))

#4th program#
n = lambda num : num ** 2
print(n(10))

#5th program#
o = lambda no : no % 2 == 0
print(o(4))

#6th program#
p = lambda q : q[::-1]
print(p('ArunTheja'))

#7th program#
r = lambda s, t : s + t
print(r(10, 20))

#8th program#
u = lambda v : len(v)
print(u('This is ATK'))


# """ SET - it will not allow duplicate values and it have only unique values. """ #

set1 = [1, 2, 1, 3, 2, 1, 3, 4, 2]
print(set(set1))

set2 = {5, 6, 7}
set2.clear()
print(set2)

set3 = {8, 9, 10}
set4 = set3.copy()
print(set4)

set5 = 'arun theja'
print(set(set5))

set6 = 'arun'
print(frozenset(set6))

set7 = {11, 12, 13}
set8 = {14, 12, 15}
print(set7.difference(set8))


# """ MAP """ #

map1 = [16, 17, 18, 19, 20]
map2 = map(lambda x : x + 5, map1)
print(map2)


# """ FILTER """ #

filter1 = range(10)
print(filter(lambda num : num > 3, filter1))
    

# """ DECORATOR """ #

#1st program#
def world(func):
    def message():
        print('************')
        func()
        print('@@@@@@@@@@@@')
    return message
def text():
    print("Arun Theja Kumar")
atk = world(text)
atk()

#2nd program#
def hello(name='jose'):
    def greet():
        return '\t HI'
    def welcome():
        return '\t HELLO'
    if name == 'jose':
        return greet
    else:
        return welcome
x = hello()
print(x())

#3rd program#
def hello(name='jai'):
    print("The HELLO() function")
    def great():
        return 'MAHESH'
    def greek():
        return 'Babu'
    print(great())
    print(greek())
hello()

#4th program#
def hellos(name='ji'):
    return 'my name is ' + name
print(hellos())
y = hellos
print(y())

#5th program#
def hack():
    return 'Pawan'
def other(func):
    print("other code goes here!")
    print(func())
other(hack)


# """ ENUMERATE """ #

enumerate1 = ['a', 'b', 'c']
for count, item in enumerate(enumerate1):
    print(count)
    print(item)

enumerate2 = ['d', 'e', 'f']
for con, no in enumerate(enumerate2):
    if con >= 2:
        break
    else:
        print(no)


# """ ZIP """ #

zip1 = [100, 101, 102]
zip2 = [103, 104, 105]
print(zip(zip1, zip2))

zip3 = ['A', 'B', 'C']
zip4 = ['D', 'E']
print(zip(zip3, zip4))

zip5 = [106, 107, 108, 109, 110]
zip6 = [111, 107, 112, 99, 98]
for zip7 in zip(zip5, zip6):
    print(max(zip7))

zip7 = [113, 114, 115]
zip8 = [116, 117, 118]
print(map(lambda zip9 : max(zip9), zip(zip7, zip8)))

zip9 = {'a':1, 'b':2}
zip10 = {'c':3, 'd':4}
print(zip(zip9, zip10))

zip11 = [119, 120, 121]
zip12 = [122, 123, 124, 125, 126]
for a,b in zip(zip11, zip12):
    print(a)
    print(b)

zip13 = [127, 128, 129]
zip14 = [130, 131, 132, 133, 134]
for c,d in zip(zip13, zip14):
    if c > d:
        print(c)
    else:
        print(d)


# """ GENERATORS """ #

def gen():
    word = ' '
    for chi in 'spam':
        i = word + chi
        yield i
print(list(gen()))


# """ FUNCTIONAL PROGRAMMING """ #

def addition(x,y):
    return x + y
def multiplication(x,y):
    return x * y
def add(func, x, y):
    return func(x,y)
print(add(addition, 5, 6))
print(add(multiplication, 7, 2))
