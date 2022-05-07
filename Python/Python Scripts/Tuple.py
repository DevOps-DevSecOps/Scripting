# """ TUPLE - It is a sequence of immutable python. The tuple cannot be changed the elements and it is only readable. It enclosed with 'PARENTHESES ()' """ #

print(type(()))

tuple1 = (1, 2, 3)
print(tuple1[0])

tuple2 = (4, 5, 6, 7, 8, 9)
print(tuple2[1:])
print(tuple2[:4])
print(tuple2[1:4])

tuple3 = ("Atk", 1994, 'python')
(name, age, code) = tuple3
print(name, age, code)

tuple4 = ('arun', 'theja')
print(len(tuple4))

tuple5 = ('Python ') * 3
print(tuple5)

tuple6 = (10, 11, 12, 13)
tuple7 = ('great', 'greet')
tuple8 = (tuple6, tuple7)
print(tuple8)

tuple9 = (14, 15, 16)
tuple10 = ('jack', 'reacher')
print(tuple9 + tuple10)

tuple11 = [17, 18, 19]
print(tuple(tuple11))

print(tuple("TOM CRUISE"))

tuple12 = ("kumar")
tuple13 = 3
for tuple14 in range(tuple13):
    print(tuple12, tuple14)

tuple15 = 'mission', 'impossible'
print(tuple15)

tuple16 = ('message')
print(tuple16[2:5])

tuple17 = (20, 21, 22)
tuple17[1] = 23
print(tuple17)

tuple18 = (20, 21, 22)
del tuple18
print(tuple18)

