# """ RESERVED KEYWORDS - cannot be used as the name of the variables. """ #
import keyword
print(keyword.kwlist) #it show all the 'Reserved keywords'


# """ VARIBLE TYPES - start with 'Letter (A to Z, a to z) or 'Underscore _' symbol and then don't start with number and don't include special characters in variable names. """ #

A = 123   #Here A is variable name, 123 is value name
B = 50.00 #Here B is variable name, 50.00 is value name
print(A)

_arun = 2.1     #varible started with Underscore '_' symbol
_123 = 'Jack' 
print(_arun)
print(_123)

arUN_1993 = 'Reacher'   #variable name can contain Letters, Number, Underscore
print(arUN_1993)

c = 'arun'
d = "theja"
d = c             #its equal d varible to c vriable as value
print(d)
print(c == d)     #to check both variables are equal or not
print(d is c)     #its true or not

E = 6.7
E = '''kumar'''  #assigning value to same variable
print(E)

F = 753
g = """tom cruise"""
F,g = g,F        #Here variables F,g swap as g,F
print(F)
print(g)

h = _45 = I_6 = 100    #Here one value(100) assigned to 3 variables(h = _45 = I_6)
print(h)
print(_45)
print(I_6)

J, _k7, l = 1994, 'mission', "impossible"      #Here 3 variables (J, _k7, l) are equal to 3 values(1994, 'mission', "impossible")
print(J)
print(_k7)
print(l)
print(J, _k7, l)

My_Name = "ATK"
print(My_Name)

THE_TOTAL_MEMBER = 80
print(THE_TOTAL_MEMBER)

this_is_a_normal_float = 42.369
print(this_is_a_normal_float)


# """ Data Types """ #
'''Integer as int, it is a whole number'''
int = 100
print(int)

'''Float act as a 'decimal' points, by using DOT(.)'''
float = 100.0
print(float)

'''String as str; collection of character to machine language; it is created by Quotations like single('), Double("), Tripple(''' ''' or """ """); includes a-z,A-Z,0-9. '''
str = 'arun',"theja",'''kumar''',"""1993""" 
print(str)

'''Complex'''
print(2j-1)
print(complex(2,3))
print(complex(10,1))
