# """ DICTIONARIES - it accessed via 'KEY' and not their index position and don't repeat the same KEY. Any key of the dictionary is associated to a value. It enclosed by 'FLOWER bracket or CURLY bracket {}'. It is mutable & read and writeable programmable. Then value can be assigned and accessed using Square bracket[]. """ #

print(type({}))

#1st program#
dict1 = {1:'hello', 'a':'world', 2:[1,2,3], 3:567}
print(dict1[1])
print(dict1['a'][2])
print(dict1[2][1])
print(dict1[3])

#2nd program#
dict2 = {4:'hai', 4:'bye', 5:[4,5,6]}
print(dict2[4])

#3rd program#
dict3 = {'A':'Arun', 'T':'Theja'}
dict3['K'] = 'Kumar'
dict3[1] = 'Thota'
print(dict3)

#4th program#
dict4 = {6:'sayhi', 7:'seeu', 8:'goodnight'}
dict4[6] = 'hero'
print(dict4)

#5th program#
dict5 = {9:22, 'b':45, 10:'abc'}
del dict5[9]
print(dict5)

#6th program#
dict6 = {11:'tom', 'c':'cruise', 'd':1994}
dict6.clear()
print(dict6)

#7th program#
dict7 = {12:11, 13:22, 14:33}
dict7[13] = dict7[13] - 20
print(dict7[13])
print(dict7.get(8,5) - dict7.get(14,9))
print(dict7)

#8th program#
dict8 = {}
dict8['one']=198
dict8['two']=143
print(dict8)

#9th program#
dict9 = dict8['one'] + 102
print(dict9)

#10th program#
dict10 = {'e':103, 'f':115}
dict10['e'] = dict10['e'] + 123
print(dict10)
print(dict10['f'] - 105)

#11th program#
dict11 = {'BMW':{'model':'550i', 'year':2016}, 'BENZ':{'model':'E350', 'year':2015}}
dict12 = dict11['BMW']['year']
print(dict12)

#12th program#
dict13 = {'g':'Jack Reacher', 'h':'MissionImpossible'}
print(dict13['g'][::-1])
print(dict13['h'].upper())
print(dict13.keys())
print(dict13.values())
print(dict13.items())

#13th program#
dict14 = {'i':[{'nested-key':['this is deep', ['hello']]}]}
print(dict14['i'][0]['nested-key'][1][0])

#14th program#
dict15 = {'j':[78, 98, {'k':['this is tricky', {'toughie':[66, 77, ['go..!..']]}]}]}
print(dict15['j'][2]['k'][1]['toughie'][2][0])
