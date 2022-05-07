#1st program#
try:
    raise ValueError
except ValueError:
    print("ValueError Exception!")

#2nd program#
try:
    Ex = ValueError()
    Ex.strerror = "value must be with in 1 and 10."
    raise Ex
except ValueError as e:
    print("valueError Exception!", e.strerror)

#3rd program#
try:
    raise ValueError('BYEE')
except ValueError as x:
    print(x)

#4th program#
def ExceptionHandling():
    try:
        a = 10
        b = 20
        c = 0
        d = (a + b) / c
        print(d)
    except:
        print("This is not Possible")
ExceptionHandling()

#5th program#
def Exception():
    try:
        e = 11
        f = 'String'
        g = 0
        print((e + f) / g)
    except ZeroDivisionError:
        print("Zero Division")
    except TypeError:
        print("TypeError")
Exception()

#6th program#
def Handling():
    try:
        h = 10
        i = 20
        j = 0
        k = (h + i) / j
        print(d)
    except ZeroDivisionError:
        print("Zero Division")
    except TypeError:
        print("TypeError")
Handling()

#7th program#
try:
    2 + 'atk'
except TypeError:
    print('Its an TypeError')
finally:
    print("Its closed")

#8th program#
try:
    file = open('text.txt', 'r')
    print(file.read())
except:
    print('Error in writing file')
else:
    print("Check Text File")

#9th program#
try:
    file = open('text.txt', 'w')
    file.write('HI Hello')
except:
    print('Error in writing file')
else:
    print("Text has been written")

#10th program#
try:
    file = open('text.txt', 'w')
    file.write('HI Hello SeeU')
finally:
    print("Execute finally code block")

#11th program#
def excepts():
    try:
        value = int(raw_input("Enter a value: "))
    except:
        print("Look its not add")
    finally:
        print("finally block executed")
    print value
excepts()

#12th program#
def excepted():
    try:
        value = int(raw_input("Please Enter a value: "))
    except:
        print("Look like you did not enter a integer!")
        value = int(raw_input("Try-Again Please Enter a value: "))
    finally:
        print("finally block executed")
    print value
excepted()

#13th program#
def program():
    while True:
        try:
            value = int(raw_input("Please Enter a Number: "))
        except:
            print("Look like you did not enter a integer!")
            continue
        else:
            print("Correct that is an integer!")
            break
        finally:
            print("finally block executed")
        print value
program()

#14th program#
try:
    print('1' + 1)
except TypeError:
    print("Error")
finally:
    print('last execution')

#15th program#
try:
    l = 22
    m = 33
    n = 44
    print(l + m) / n
except:
    print("IN the Except BLOCK")
else:
    print("there was no exception")

#16th program#
def programed():
    while True:
        try:
            No = input("Enter a no: ")
            print("the value no is: ", No ** 2)
        except:
            print("Error Occured")
            continue
        else:
            break
programed()

#17th program#
try:
    p = 5
    q = 0
    print(p / q)
except:
    print("Division Occured")
finally:
    print("its end")

#18th program#
try:
    for r in ['A', 'B', 'C']:
        print(r**2)
except:
    print("Error")
    
