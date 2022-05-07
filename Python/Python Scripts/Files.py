 # """ READ FILES """ #

#1st program#
read1 = open('ATK.txt','r')
print(read1.read())
read1.close()

#2nd program#
read2 = open('ATK.txt','r')
print(read2.read(23))
read2.close()

#3rd program#
read3 = open('ATK.txt','r')
print(read3.read()) [9:35]
read3.close()

#4th program#
read4 = open('ATK.txt','r')
for arun in read4.read():
    print(arun)
read4.close()

#5th program#
read5 = open('ATK.txt','r')
for theja in read5:
    print(theja)
read5.close()

#6th program#
read6 = open('ATK.txt','r')
for kumar in read6.readline():
    print(kumar)
read6.close()

#7th program#
read7 = open('ATK.txt','r')
print(read7.readlines())
read7.close()


# """ WRITE FILES """ #

#1st program#
write1 = open('kta.txt','w')
write1.write("I written the text in notepad \n")
write1.write("GOOD BYE")
write1.close()

#2nd program#
write2 = open('kta.txt','w')
write2.write("I written the text in notepad \n")
write2.write("GOOD BYE")
write2.close()
write2 = open('kta.txt','r')
print(write2.read())
write2.close()

#3rd program#
write3 = open('kta.txt','r')
print(write3.read())
write3.close()
write3 = open('kta.txt','w')
write3.write("See you soon")
write3.close()
write3 = open('kta.txt','r')
print(write3.read())
write3.close()

#4th program#
write4 = open('kta.txt','r')
print(write4.read())
write4.close()
write4 = open('kta.txt','w')
write4.write("GOOD MORNING")
write4.close()

#5th program#
write5 = open('kta.txt','w')
write5.write("GOOD MORNING's")
write5.close()
write5 = open('kta.txt','r')
print(write5.read())
write5.close()

#6th program#
write6 = open('kta.txt', 'r')
write7 = write6.read()
write6.close()
write8 = open('kta.txt', 'w')
write8.write("How are You?")
write8.close()


# """ WORKING with FILES """ #

#1st program#
work1 = open('Files.py', 'r')
print(work1.read())
work1.close()

#2nd program#
work2 = open('Files.py', 'r')
work3 = work2.read()
print(work3)
work2.close()


# """ EXCEPTIONS with FILES """ #

#1st program#
try:
    exc1 = open('exc.txt')
    print(exc1.read())
finally:
    exc1.close()

#2nd program#
try:
    exc2 = open('exc.txt')
    exc3 = exc2.read()
    print(exc3)
finally:
    exc2.close()

# 3rd program#
try:
    with open('exc.txt', 'r') as exc4:
        print(exc4.read())
finally:
    exc4.close()

#4th program#
try:
    exc5 = open('exc.txt')
    print(exc5.read())
    #print(1/0)
finally:
    exc5.close()


# """ OVER WRITING FILES """ #
over1 = open('exc.txt', 'r')
over2 = over1.read()
over1.close()
over3 = open('exc.txt', 'w')
over3.write(over2)
over3.write("Thank YOU")
over3.close()
over4 = open('exc.txt', 'r')
print(over4.read())
over4.close()


# """ FORMAT FILES - Read Binary & Write Binary """ #

#1st program#
format1 = open('iot.gif', 'rb')
format2 = format1.read()
format1.close()
format3 = open('at.gif', 'wb')
format3.write(format2)
format3.close()

#2nd program#
format4 = open('gAtom.exe', 'rb')
format5 = format4.read()
format4.close()
format6 = open('atom.exe', 'wb')
format6.write(format5)
format6.close()
