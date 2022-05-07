# """ FUNCTION - its define using the block keyword 'def' followed with function name as the block name. It convenient way to divide your code into usefull blocks, allowing us to order our code, make it more readable, reuse it and save time. Also function are key way to define interface so programmer can share their code. """ #

#1st program#
def arun(a,b):         #Here def is new function, arun is function name, (x,y) is parameters or arguments
    print(a + b)
arun(1, 5)             

#2nd program#
def theja(c,d):
    print(c - d)
    print(c * d)
theja(5, 10)

#3rd program#
def kumar(e,f):
    print(e / f)
    print(e ** f)
    print(e % f)
kumar(15, 20)
kumar(20, 25)
kumar(25, 30)
kumar(30, 35)

#4th program#
def atk(g,h):
    print(g / h)
    print(g ** h)
    print(g % h)
atk(35, 40)
atk(40, 45)
atk(45, 50)

#5th program#
def ATK(i, j):
    print(i + j)
for AT in range(1, 4):
    k = int(input('Enter a no:'))
    l = int(input('Enter another no: '))
    ATK(k, l)

#6th program#
def Hulk(m, n):
    print(m - n)
q = int(input('Enter value: '))
r = int(input('Enter another value: '))
Hulk(q, r)

#7th program#
def Thor(u, v):
    return(u * v)
w = Thor(444, 555)
print(w)

#8th program#
def Avengers(x, y):
    return(x / y)
z = int(input("Enter: "))
A = int(input("Enter another: "))
B = Avengers(z, A)
print(B)

#9th program#
def Ironman(B, C):
    return(B + C)
for D in range(1,4):
    E = int(input('Number: '))
    F = int(input('another Number: '))
    print(Ironman(E, F))

#10th program#
def CaptainAmerica(G):
    H = G ** 2
    return H
I = CaptainAmerica(2)
print(I)

#11th program#
def AntMan(J):
    return J ** 2
print(AntMan(4))

#12th program#
def Spiderman(K):
    print('Hi ' + K + ' !')
L = ['RACHEL', 'MONICA', 'PALAVI']
for K in L:
    Spiderman(K)
    print('Next girls')

#13th program#
def DoctorStrange(L):
    return L % 2 == 0
M = DoctorStrange(10)
print(M)

#14th program#
def BlackPanther(N, O=2):
    return N + O
P = BlackPanther(4, O=12)
print(P)

#15th program#
def Q():
    return 1
print(Q())

#16th program#
def Marvel(R):
    S = ['sfo', 'nyc', 'la']
    if R in S:
        return True
    else:
        return False
T = Marvel("sfo")
print(T)

#17th program#
U = 10
def Marvels(U):
    print('value of local U is: ' + str(U))
    U = 2
    print("new value of local U is: " + str(U))
print('value of global U is: ' + str(U))
Marvels(U)
print("Did the value of global U change ?" + str(U))
