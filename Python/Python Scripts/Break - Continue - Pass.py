# """ BREAK statement - It terminates the current loop and resumes execution at the next statement, just like the traditional break statement in c. The most common use for break is when some external condition is triggered requiring a hasty exit from a loop.Terminate the loop statement and transfer execution to the loop statement immediate following the loop.""" #

#1st program#
for i in range(10):
    if i == 6:
        print("STOP")
        break
    else:
        print(i)

#2nd program#
x = 0
while x < 10:
    print("x is currently: " + str(x))
    x = x + 1
    if x == 3:
        print("Hey X equals 3!")
        break
    else:
        print("CONTINUING")
        continue

#3rd program#
x = 0
while x < 10:
    print("Value of x is: " + str(x))
    x = x + 1
    if x == 8:
        break
        print("STOP")
    print("It's done")
print("Just brake the loop")


# """ CONTINUE statement - It return the control to the beginning of the while loop. It rejects all the remaining statement in the current iteration of the loop and moves the control back to top of the loop. """ #

#1st program#
for i in range(10):
    if i == 6:
        print("SKIP 6")
        continue
    else:
        print(i)
print("BYE")

#2nd program#
x = 0
while x < 10:
    print("x is currently: " + str(x))
    x = x + 1
    if x == 3:
        print("Hey X equals 3!")
    else:
        print("CONTINUING")
        continue

#3rd program#
x = 0
while x < 10:
    print("Value of x is: " + str(x))
    x = x + 1
    if x == 8:
        print("X is equals to 8!")
        continue
print("10 is not less than 10")


# """ PASS statement - It is used when a statement is required syntactinally but you do not want any command or code to execute and also it is a null operation, nothing happens when it executes. """ #

#1st program#
for i in range(10):
    if i == 5:
        print("PASS 5")
        pass
    else:
        print(i)
