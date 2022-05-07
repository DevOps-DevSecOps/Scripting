# """ LIST:- it is one of the simplest and most important data structure in python. It is enclosed with 'SQUARE Bracket[]' and each item is separate by a commma (,). It is collection of item where each item in the list has an assign index value. we can use range in list method. It is read and writeable program and also it is mutable. """ #

print(type([]))

list1 = [1,2,3,'a','b','c']  #[1,2,3,'a','b','c'] - 0, 1, 2, 3, 4, 5
print(list1[1])              #Here 1 is index
print(list1[4])              #Here 4 is index

list2 = [4,5,6,'d','e','f']
print(len(list2))            #length of the elements

list3 = [7,8,9,'g','h','i']
print(list3.pop())           #it will take last element default and finally it remove element
print(list3.pop(2))          #By using 2 index removing element from list
print(list3)

list4 = [10, 2.5, 'Hello World!', 2.5, 34]
print(list4 * 2)              #multiplying of list
print(list4[2] * 3)
print(list4 + ['atk'])        #Adding an element in the list
print(list4.count(2.5))       #count no of elements
print(list4.index(2.5))       #Here 2.5 is an element to find the index number
print(list4[1] + list4[4])    #Here 2 and 4 for index, by using index extract elements values addition operation has been didit

list5 = [1994, 'arun', 'theja', 'kumar', 'ATK', 'Tom', 'Cruise']   #[10, 'arun', 'theja', 'kumar', 'ATK', 'TOM', 'CRUISE'] these are 7 elements
print(list5[0:2])                                                  #Here slice operation
print(list5[2:5])
print(list5[1:])
print(list5[:3])

list6 = [1994, "Tom", "Cruise"]             #[10, 'Tom', "Cruise"] these are 3 elements
list6.append("MISSION IMPOSSIBLE")          #append is adding element at end
list6.append([19,94])
print(list6)

list7 = [1,2,3,4,5]     #[1,2,3,4,5] - 0, 1, 2, 3, 4
list7.insert(4, 6)      #Here 4 is index, and 6 is value
list7.insert(3, 9)      #Here 3 is index, and 9 is value
list7.insert(0, 'HI')
list7.insert(8, 'BYE')
print(list7)            #insert used to insert the values

list8 = ["Tom", "Cruise", "JACK REACHER"]
list8.remove("Tom")                          #remove element from list
print(list8)

list9 = ['Ethan', 'Hunt', "Jack Reacher"]
list9.reverse()                              #it reverse the element fom last to start
print(list9)

list10 = [11,12,13,[14, 15, 16]]
list10[3][1] = 'HahaHa'
print(list10)

list11 = ['hello', 'world']
list11[2:] = 'foo'          #Here slice operation
list11[:0] = 'Hmm'
print(list11)

list12 = ['Mission', 'Impossible']
list12 = list12 + ['Ethan Hunt'] + list12
print(list12)

list13 = [17, 18, 19, 'ATK', 'atk', '@A!t^K#']
list13[2] = 5
list13[5] = 'Mahesh Babu'
print(list13)

list14 = ['a', 'b', 'e', 'g', 'c', 'f', 'd']
list14.sort()
print(list14)

list15 = [20, 21, 22]
list16 = [23, 24, 25]
list17 = [26, 27, 28]
list18 = [list15, list16, list17]
print(list18)
print(list18[0][1])
print(list18[1][2])
print([row[0] for row in list18])

list19 = [29, 30, 31]
list19.extend([32, 33])
print(list19)

print([35, 36, 37] + [38, 39, 40])

print(['Hi!'] * 4)

for list20 in [41, 42, 43]:
    print(list20)

list21 = ['abcd', 44, 45.0]
list22 = [123, 'efgh']
print(list21 + list22 * 2)
