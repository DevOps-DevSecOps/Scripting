# """ CLASSES:- """ #

#1st program#
class A:
	def __init__(self,x,y):
		self.x=x
		self.y=y
class B:
	def __init__(self,z):
		self.z=z
a=B('arun')
print(a.z)
b=A('theja',6)
print(b.x)
print(b.y)

#2nd program#
class Cat:
	def __init__(self,color,legs):
		self.color=color
		self.legs=legs
felix=Cat("ginger",4)
rover=Cat("blue",5)
stumpy=Cat("brown",3)
print(felix.color)
print(rover.legs)

#3rd program#
class Cat:
	def __init__(self,x,y):
		self.color=x
		self.legs=y
felix=Cat('ginger',4)
rover=Cat('blue',5)
print(felix.color)
print(rover.legs)

#4th program#
class Human:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def type(self):
		print(self.name)
		print(self.age)
H1=Human('arun',23)
print(H1.type())
H2=Human('theja',24)
print(H2.type())

#5th program#
class Car(object):
        def __init__(self, make):
                self.make = make
c1 = Car('bmw')
c2 = Car('benz')
print(c1.make)
print(c2.make)

#6th program#
class Bike(object):
        def __init__(self, made, model='550i'):
                self.made = made
                self.model = model
c3 = Bike('bmw')
print(c3.made)
print(c3.model)
c4 = Bike('benz')
print(c4.made)
print(c4.model)

#7th program#
class Jet(object):
        wheels = 3
        def __init__(self, version, color):
                self.version = version
                self.color = color
        def info(self):
                print('Jet of version: ', self.version)
                print('Jet model: ', self.color)
c5 = Jet('Race', 'White')
print(c5.version)
c5.wheels = 2
print(c5.wheels)
c5.info

c6 = Jet('Funk', 'red')
print(c6.color)
print(c6.wheels)
c6.info

#8th program#
class Player(object):
        def __init__(self, bankroll=100):
                self.bankroll = bankroll
        def add_bankroll(self, amount):
                self.bankroll += amount
sam = Player(bankroll = 1000)
print(sam.bankroll)
print(sam.add_bankroll(20000))


# """ INHERITANCE:- """ #

#1st program#
class Wolf:
	def __init__(self,name,color):
		self.name=name
		self.color=color
	def bark(self):
		print('Go...')
class Dog(Wolf):
	def goal(self):
		print('woof')
Husky=Dog('Max','grey')
Husky.bark()
Husky.goal()

#2nd program#
class Hulk(object):
        def __init__(self):
                print('HellO')
        def drive(self):
                print('start')
        def slow(self):
                print('slow')
class Thor(Hulk):
        def __init__(self):
                Hulk. __init__(self)
                print('bYe')
c7 = Hulk()
c7.drive()
c7.slow()

c8 = Thor()
c8.drive()
c8.slow()


# """ OVERRIDING:- """ #

#1st program#
class A:
	def __init__(self,x,y):
		self.x=x
		self.y=y
class B(A):
	def __init__(self,z):
		self.z=z
a=A(5,6)
b=B(4)
print(a.x)
print(b.z)
#print(b.x)

#2nd program#
class Car(object):
        def __init__(self):
                print("you just created the car instance")
        def drive(self):
                print("Force")
        def stop(self):
                print("High")
class BMW(Car):
        def __init__(self):
                Car. __init__(self)
                print("You just created the Animation")
        def drive(self):
                super().drive()
                print("U R fighting now....")
        def handsup(self):
                print("This is unique feature")
c9 = Car()
c9.drive()
c9.stop()

c10 = BMW()
c10.drive()
c10.stop()
c10.handsup()
