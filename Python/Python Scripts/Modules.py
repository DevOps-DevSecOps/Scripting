# """ MATH Module - is a standard module in python and is always availables. To use mathematical functions under this module, you have to import the module by using import math. """ #

import math
print(dir(math))              #here u can see math module commands

print(math.acos(1))
print(math.acosh(2))
print(math.asin(1))
print(math.asinh(2))
print(math.atan(46))
print(math.atan2(4, 5))
print(math.atanh(0))
print(math.radians(5))
print(math.floor(9.6))
print(math.log(2))
print(math.log10(10))
print(math.log1p(56))
print(math.fabs(7))
print(math.modf(78))
print(math.isinf(7))

import math as a                #here math as(alias) a
print(a.ceil(2.5))
print(a.copysign(5, 9))
print(a.cos(2))
print(a.cosh(3))
print(a.degrees(7))
print(a.e)
print(a.erf(3))
print(a.erfc(4))
print(a.exp(4))
print(a.expm1(7))

from math import sqrt as square_root
print(square_root(10000))

from math import trunc
print(trunc(3))

from math import sin, sinh, tan, tanh
print(sin(3))
print(sinh(6))
print(tan(4))
print(tanh(5))

import math as atk              #here math as(alias) atk
print(atk.factorial(7))
print(atk.fmod(8, 5))
print(atk.frexp(6))
print(atk.isnan(3))
print(atk.ldexp(2,2))
print(atk.lgamma(3))
print(atk.pow(2,5))
print(atk.pi * 5)
print(atk.gamma(6))
print(atk.hypot(3, 6))
print(atk.isinf(333*32))
print(atk.fsum([10, 11]))
print(atk.fsum(range(1,4)))
print(atk.modf(10.12))


# """ RANDOM Module - provide access to function that support many operations. The most important things is that allows you to generate random numbers. """ #

import random
print(dir(random))
