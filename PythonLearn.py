from operator import mul
import os

def fruitList():
    define="#Lists"
    fruitList=["Apple","Cherry"]
    print("My List:",fruitList,define)

    fruitList.append("Lemon")
    print(len(fruitList))

    for i in fruitList:
        print(i)

def myTuple():
    myTuple=tuple(["Max", 28, "SomethingHere"])
    print("My Tuple:", myTuple, "#Tuples use () instead of [], faster, less memory")

def dictionaryOnenTwo():
    define="#Dictionaries use {} or var=dict(key=\"value\")"
    dictionaryOne=dict(name="Arti", age="27", city="Holiday")
    print(dictionaryOne, define)

    dictionaryOne["email"]="somewhere@mail.com" #Adds "email": "mail.com" to dictionary
    print(dictionaryOne, define)

    dictionaryAlternate={"country":"US", "name":"Flarty"}
    print("Alternate way:", dictionaryAlternate)

    dictionaryOne.update(dictionaryAlternate) #Merge dictionaryOne & dictionaryAlt
    print("Merging dictionary:", dictionaryOne)

    if "name" in dictionaryOne:
        print("If name in dictionary, print:", dictionaryOne["name"])

    try: #Try/Except alternative to if statement
        print("Try/If statements alternate to if:",dictionaryOne["name"]) 
    except:
        print("Error")

    for key in dictionaryOne:
        print("If key in Dictionaryone, print key:", key)

    for key in dictionaryOne.keys(): #Selects keys
        print(key)

    for value in dictionaryOne.values(): #Selects values
        print(value)

    for key, value in dictionaryOne.items(): #Selects both keys & values
        print(key, value)

def mySet():
    define="#Sets are Unordered, Mutable, No Duplicates"
    mySet={1,2,3}
    print("My Set:", mySet,define)

    mySetAlternate=set([1,2,3])
    print("My Set Alternative:", mySetAlternate,define)

    mySetOdds={1,3,5}
    mySetEvens={2,4,6}
    mySetPrimes={2,3,5}
    u=mySetOdds.union(mySetEvens) #Combines elements
    print("Union:", u,define) 

    intersect=mySetOdds.intersection(mySetPrimes) #Combines like elements
    print("Intersection:", intersect,define) 

    diff=mySetEvens.difference(mySetPrimes,mySetOdds) #Differences in elements
    print("Difference:", diff, define)

def readFile():
    ##r"FULLPATH" is raw file path##
    ##Below line lists contents in directory##
    for f in os.listdir(r"C:\Users\jslicker\Documents\Python"):
            print(f)
    employee_file = open(r'C:\Users\jslicker\Documents\Python\TestFile.txt', "r")
    print(employee_file.readable()) #Will tell if can read from file
    print(employee_file.read()) #Will read all contents of file
    print(employee_file.readline()) #Will read each line
    print(employee_file.readline()) #Will read each line
    print(employee_file.readlines()) #Will be array of items
    for employee in employee_file.readlines():
        print(employee) #Will print each employee in file
    employee_file.close() #Need to always close file afterwards

def writeFile():
    employee_file=open(r'C:\Users\jslicker\Documents\Python\TestFile.txt', "a")
    employee_file.write("\nArti / Accounting") #Append to file
    employee_file.close()
    employee_file=open(r'C:\Users\jslicker\Documents\Python\TestFile.txt', "w")
    employee_file.write("\nArti -- Accounting") #Write new file
    employee_file.close()

def string():
    myString="        Hello World"
    myString=myString.strip() #Removes whitespace
    print(myString, "#Removing Whitespace with .strip() method")
    print(myString.upper(), myString.lower(), "#Upper and Lower with upper(), lower() methods")
    print(myString.endswith('Hello')) #Returns boolean value 
    print(myString.find('o')) #Returns indexm -1 if character/substring not found
    print(myString.count('p')) #How many characters in string
    print(myString.replace('World', 'Universe')) #Replaces first word with second

    myList=myString.split(",") #Converts string to list
    print(myList)

    newString=''.join(myList) #Converts list back to string, preferred as cleaner & faster than 'for i in myList: myString+=i
    print(newString, '\n')

    var="UsernameOne"
    var2="UsernameTwo"
    var3="NewVariable1"
    var4="NewVariable2"
    myVar="The variable is %s" % var #Old format
    print(myVar)
    varNum=3

    myNum="The variable is %d" % varNum #Old format
    print(myNum)
    varFloat=5.512

    myFloat="The variable is %.2f" % varFloat #Old format, %.2f = two decimal places
    print(myFloat)

    myVar="The variable is {} and {}".format(var,var2)#New Format, multiple variables with "{} and {}".format
    print(myVar)

    myVar=f"The variable is {var3} and {var4}" #f is New Format, fastest
    print(myVar, "#New Method")

    myFloat="The variable is {}".format(varFloat) #New Format, using .format method with variable argument
    print(myFloat)

    myFloat="The variable is {:.2f}".format(varFloat) #New Format, :.2f = two decimal places
    print(myFloat)

def myCollections(): #Collections are containers that stores elements as dictionary keys and values
    from collections import Counter 
    a="aaaaaabbbbbbccccccdddd"
    myCounter=Counter(a)
    print("My Dictionary via Counter:", myCounter)
    print("My keys: ", myCounter.keys())
    print("My Values:", myCounter.values())
    print(myCounter.most_common(1))
    print("My list of elements: ", list(myCounter.elements()))

    from collections import namedtuple
    Point=namedtuple('Point', 'x,y') #Typically argument is same as variable, creates class Point w fields x & y
    pt = Point(1,-4)
    print(pt) 
    print("Values for x & y: ", pt.x,pt.y)   

    from collections import OrderedDict #Python 3.7 remembers order, but older versions dont have ordered dictionaries
    orderedDict=OrderedDict()
    orderedDict['a'] = 1
    orderedDict['b'] = 2
    orderedDict['c'] = 3
    orderedDict['d'] = 4
    print (orderedDict)

    from collections import defaultdict
    d=defaultdict(int)
    d['a'] = 1
    d['b'] = 2
    print(d)
    print(d['a'], d['b']) #default integer 0 if non-existent

    from collections import deque #Double ended queue, allows remove elements from both ends
    deq = deque()
    deq.append(1)
    deq.append(2)
    deq.appendleft(3) #Add to beginning of element
    print(deq)
    deq.popleft() #Remove beginning element
    print(deq)
    deq.extendleft([4,5,6])
    print(deq)
    deq.rotate(2)
    print(deq)

def iterTools(): #Iterators data types in for loops like lists
    from itertools import product, permutations, combinations_with_replacement, combinations, accumulate, groupby
    import operator
    a=[1,2]
    b=[3]
    prod = product(a,b) #repeat=2)
    print(list(prod))

    a=[1,2,3,4]
    perm=permutations(a, 2) #Provides range of 2, can just put argument of a
    #print("Permuations:", list(perm))

    comb=combinations(a,2)
    print("Combinations", list(comb))

    comb_wr=combinations_with_replacement(a,2)
    print("Combinations with replacements:", list(comb_wr))

    acc=accumulate(a, func=mul)
    print("Accumulate:", a)
    print("Accumulate list:", list(acc)) #1+2=3, 3+3=6, 6+4=10, computes sums

    def smaller_than_3(x):
        return x < 3
    group_obj=groupby(a, key=smaller_than_3)
    for key, value in group_obj:
        print("Groupby:", key,list(value))

    from itertools import count,cycle,repeat
    for i in count(10): #Infinite loop starting at 10.
        print(i)
        if i == 15: #Breaks loop if at 15
            break

    #a=[1,2,3]
    #for i in cycle(a): #Infinite loop of 1,2,3 and 1,2,3.
    #    print(i)
    #    if i == 15: #Breaks loop if at 15
    #        break

    a=[1,2,3]
    for i in repeat(1, 4): #Repeats 1, 4 times
        print(i)

def lambdaFunction(): #One line function that looks like lambda arguments: expression
    add10=lambda alababa: alababa+10
    print("Lambda Function:", add10(5))

    def add10_func(x): #Same as above, except not 1 line
        return x+10
    print("Not lambda function:", add10_func(5))

    mult=lambda x,y: x*y
    print("Also Lambda 2 arguments:", mult(2,7))

    points2DList=[(1,2),(15,1),(5,-1),(10,4)]
    points2DListSorted=sorted(points2DList)
    print("2D List, unsorted:", points2DList)
    print("2D List Sorted:", points2DListSorted)

    a=[1,2,3,4,5,10]
    b=map(lambda x: x*2, a) #map(func,seq)
    print("Map Lambda: ", list(b))

    c=[x*2 for x in a] #Same as map
    print("Same as map:", c)

    d=filter(lambda x: x%2==0, a) #Filter(func, seq) Returns true or false, returns all elements
    print("Filter:", list(d))

    e=[x for x in a if x%2==0] #Same as filter
    print("Same as filter:", e)


#Errors and Exceptions
class ValueTooHighError(Exception):
    pass

class ValueTooLowError(Exception):
    def __init__(self,message,value):
        self.message = message
        self.value = value

def test_value(x):
    if x>100:
        raise ValueTooHighError('Value is too high', x)
    if x<5:
        raise ValueTooLowError('Value too small', x)

try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooLowError as e:
    print(e.message, e.value) 

def logging(): #Defaults to warning and above printed
    import logging
    logging.basicConfig(level=logging.DEBUG, format='%(ascitime)s-%(name)s-%(levelname)s-%(message)s',
                        datefmt='%m/%d/%Y %H:%M:%S')
    logging.debug('This is a debug message')
    logging.info('This is a info message')
    logging.warning('This is a warning message')
    logging.error('This is a error message')
    logging.critical('This is a critical message')


#def checkKey(dict, keyValue):
#    dict = {'a': 100, 'b':200, 'c':300}
#    if keyValue in dict.keys():
#        print("Present, ", end ="")
#        print("value =", dict[keyValue])
#    else:
#        print("Not present")

#print("What key are you looking for?")
#keyValue=input()
#checkKey(dict, keyValue)
#fruitList()
#myTuple()
#dictionaryOnenTwo()
#mySet()
#readFile()
#writeFile()
#string()
#myCollections()
#iterTools()
lambdaFunction()

import time
start_time=time.time()
a=1000000
a=a*10000000000000000
stop_time=time.time()
print("Duration: {}".format(stop_time - start_time))
print (f"Duration: {start_time - start_time}")