# """ ARITHMETIC OPERATORS """ #
'''Integer'''
a = 6
b = 3

c = a + b      #Addition    
d = b + a
print(c)
print(d)

print(a - b)   #Substaction
print(b - a)

print (6 * 3)  #Multiplication

print(a / 3)   #Division

'''Float'''
e = 7
f = 24.9
print(e + f)
print(f - e)
print(e * f)
print(e / f)

'''String'''
g = "atk"             
h = "thota"
concatenation = g + h   #combining two sting, Except Addition(+) remaining arithmetic operators will give error
print(concatenation)

i = "1993"
j = '1994'
print(i + j)

k = "ATK"
l = 3
print(k * l)     #Except Multiplication(*) remaining arithmetic operators will give error
print(l * k)

print('1994' * 2)

'''Modules'''
m = 99 % 2
print(m)

n = 22.0 % 44
print(n)

'''Floor Division'''
print(20 // 6)
print(56 // 2.4)     

'''Exponentiation'''
o = 6 ** 9
print(o)     

'''Operations'''
print(2 + 3 - 5 * 6 / 7)    #Multiplication(*) and Division(/) will do first operators then finally remaining operators

print((2 + 4) * 3 / 2)      #In Parenthese means () will do first operator then remaining outside of parenthese operators 

print((2 + 4 * 2) * 3 / 2)  #In Parenthese Multiplication(*) will do operation then Addition(+) outside of Parenthese Multiplication & Division

'''Variable using Operators'''
p = 25

p+=10     #Addition
print(p)

p-=5      #Substraction
print(p)

p*=2      #Multiplication
print(p)

p/=5      #Division
print(p)  

p//=6     #Floor Division
print(p)

p%=19     #Modules
print(p)

p**=22    #Exponentiation
print(p)


# """ BOOLEAN OPERATORS - it is immutable. Boolean also known as bool and it have two arguments True & False. """ #
 
q = True
r = False

print(bool(0))
print(bool(1))
print(bool(2))

s = ''           #empty string
t = " "
u = """Hello"""  #assign value to variable
print(bool(s))
print(bool(t))
print(bool(u))

"""       Boolean Operators
AND condition:- 
True and True   = True
True and False  = False
False and False = False

OR condition:-
True or True   = True
True or False  = True
False or False = False

NOT condition:-
not True  = False
not False = True
"""

v = (10 == 10) and (10 > 9)
print(v)
w = (10 == 10) and (10 < 9)
print(w)
x = (10 < 10) and (10 < 9)
print(x)

y = (10 == 10) or (10 > 9)
print(y)
z = (10 == 10) or (10 < 9)
print(z)
A = (10 > 10) or (10 < 9)
print(A)

B = not (10 == 10)
print(B)
C = not (10 > 10)
print(C)

'''Boolean Precedence'''
D = True or not False and False
print(D)
E = (10 == 10) or not (10 > 10) and (10 > 10)
print(E) 
F = (10 == 10 or not 10 > 10) and 10 > 10
print(F)

'''Logical Operators'''
G = (1 < 2 and 2 < 3)
print(G)         
H = (1 < 3 > 2)
print(H)
I = (1 < 3 and 3 > 2)
print(I)
J = (1 == 2 or 2 > 1)
print(J)
K = (1 == 1 or 100 == 1)
print(K)

'''Comparision Operators'''
L = (2 == 2)
M = (1 == 0)
print(L)
print(M)

N = (2 != 1)
O = (2 != 2)
print(N)
print(O)

P = (2 <> 1)
print(P)

Q = (2 > 1)
R = (2 > 4)
S = (10 > 9)
T = (10 > 10)
print(Q)
print(R)
print(S)
print(T)

U = (2 < 4)
V = (2 < 1)
W = (10 < 10)
print(U)
print(V)
print(W)

X = (2 >= 2)
Y = (2 >= 1)
Z = (10 >= 9)
print(X)
print(Y)
print(Z)

atk = (2 <= 2)
ATK = (2 <= 10)
at  = (10 <= 9)
AT = (10 <= 11)
print(atk)
print(ATK)
print(at)
print(AT)

arun = (10 >= 11 - 1)
print(arun)
ARUN = (1 <= 10 >= 10)
print(ARUN)
