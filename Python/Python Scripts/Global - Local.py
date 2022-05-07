# """ Global variable are the one that are defined and declared outside a function and we need to use them inside a function. If variable with same name is defined the scope of function as well then it will print the value given inside the function only and not the global value. """ #

#1st program#
a = 5           #global
def add():
    a = 10      #local
    print("Value of A: " + str(a))
add() 
print("value A: " + str(a))


#2nd program#
def add():
    b = 'arun'  #local
    print("Value of B: " + str(b))
b = 'theja'     #global  
add()
print("value B: " + str(b))


#3rd program#
c = 5
def add(C):
    print("C: " + str(C))
    c = 10
    print("Value of C: " + str(c))
add(c)
print("Value C: " + str(c))


#4th program#
def add(D):
    print("D: " + str(D))
    d = 10
    print("Value of D: " + str(d))
d = 5
add(d)
print("Value D: " + str(d))


#5th program#
e = 5
print ("E: " + str(e))
def add():
    global e
    e = 10
    print("Value E: " + str(e))
add()
print("Value E: " + str(e))


#6th program#
f = 5
def add(F):
    print("F :" + str(F))
    global f
    f = 10
    print("Value of F: " + str(f))
add(f)
print("Value F: " + str(f))


#7th program#
def add(G):
    print("G: " + str(G))
    global g
    g = 10
    print("Value of G: " + str(g))
g = 5
add(g)
print("Value G: " + str(g))


#8th program#
h = 25
def printer():
    h = 50
    return(h)
print("Value of H: " + str(h))
print(printer())


#9th program#
i = 100
def func(i):
    print("i: " + str(i))
    i = 75
    print("Value of I: " + str(i))
func(i)
print("Value I: " + str(i))


#10th program#
name = "ATK"
def greet():
    name = "aruntheja"
    def hello():
        print('Hi ' + name)
    hello()
greet()


#11th program#
Value_no = 1
def func():
    global Value_no
    print("GLOBAL Value: " + str(Value_no))
    Value_no = 111
    print(Value_no)
print("CALLING FUNCTION: " + str(Value_no))
func()
print("VALUE is: " + str(Value_no))
