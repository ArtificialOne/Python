import os
from re import X
from threading import Thread, Lock, current_thread
import time
import sys
from queue import Queue
from turtle import goto
#Iterable = Python object with __iter__ or __getitem__ method defined returning iterator
#Iterator = Python object with __next__ or next method defined
#Iteration = Taking item from something like lists, the process itself


def fruitList(): #Lists use [], more memory than Tuples, mutable
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
    define="Sets are Unordered, Mutable, No Duplicates"
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
    print(myString.find('o')) #Returns index -1 if character/substring not found
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

    myVar=f"The variable is {varFloat:.2f} and {varFloat:.2f}" #f is New Format, fastest
    print(myVar, "#New Method")

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
def test_value(x):

    class ValueTooHighError(Exception):
        pass

    class ValueTooLowError(Exception):
        def __init__(self,message,value):
            self.message = message
            self.value = value

    if x>100:
        raise ValueTooHighError('Value is too high', x)
    if x<5:
        raise ValueTooLowError('Value too small', x)

    try:
        test_value()
    except ValueTooHighError as e:
        print(e)
    except ValueTooLowError as e:
        print(e.message, e.value) 

#Range returns sequence of numbers by 0 by default range(#1,#2,#3) which is 1 - 2, by #3 increments
def range_function():
    print("Input number range to end at:", end="")
    number_n=int(input())
    
    print("Input number range increment:", end="")
    number_i=int(input())

    x = range(1,number_n,number_i)
    for i in x:
        print(i)
#range_function()

def range_function_2(*args):
    for i in range(len(args)):
        print("This is for i in range(len(args), print args[i]:", args[i])
range_function_2("henry", "jilly", "addy\n")

def range_function_3(*args):
    for i in args:
        print("This is for i in args, print args:", i)
range_function_3("henry","jilly","addy""\n")

#Range returns sequence of numbers by 0 by default range(#1,#2,#3) which is 1 - 2, by #3 increments
def list_len_range_id():
    x=1
    y=2
    z=["one","two","three"]
    print(id(x))
    print(id(y), "\n")
    print("print(list(z)), the contents of container:", list(z))
    print("print len(z), how many items in container:", len(z), "\n")
    print("print range(len(z))):", (range(len(z))),"\n")
    print("print (list(range(5))), counting up to 5, not including:", (list(range(5))),"\n")
    print("print (list(range(0,20,2))) which prints 0 up to 20, increment of 2", (list(range(0,20,2))),"\n")
    for i in range(3):
        print("for i in range(3): print i (0 - 3, not including 3)):", i)
    print("\n")
    for i in range(len(z)):
        print("for range(len(z)) print z[i]: ",z[i])
    print("\n")
list_len_range_id()

def logging(): #Defaults to warning and above printed
    import logging
    logging.basicConfig(level=logging.DEBUG, format='%(ascitime)s-%(name)s-%(levelname)s-%(message)s',
                        datefmt='%m/%d/%Y %H:%M:%S')
    logging.debug('This is a debug message')
    logging.info('This is a info message')
    logging.warning('This is a warning message')
    logging.error('This is a error message')
    logging.critical('This is a critical message')

def randomNumbers():
    import random


def my_decorator(new_func):
    def wrapper():
        print("Something here first.")
        new_func()
        print("Something here after")
    return wrapper

def do_something():
    print("Here is SOMETHING")

do_something = my_decorator(do_something) #Passes do_something to new_func within my_decorator 
#do_something()


####*ARG && *KWARGS####
def var_args_func():
    def var_args(first_arg, *argv):
        print("First normal arg:", first_arg)
        for arg in argv:
            print("Another arg through *argv:", arg)

    var_args('One', 'Two', 'Three', 'Testy')

def print_name_func():
    def print_name(name): #Parameter
        print(name)

    print_name("MyNameHere") #Argument Passed
#print_name_func()


def param_argument_func():
    def param_argument(alpha,beta,charlie):
        print(alpha,beta,charlie)
    param_argument(1,2,3) #Passes 1,2,3 to a,b,c
#param_argument_func()


def param_argument_func_2():
    def param_argument(alpha,beta,charlie):
        print(alpha,beta,charlie)
    param_argument(1,beta=2,charlie=3) #Exact same as above, keyword arguments, cannot use position arguments (1) after keyword arguments
#param_argument_func_2()

def param_arg_keyword_func():
    def param_arg_keyword(alpha,bravo,charlie,delta=4):
        print(alpha,bravo,charlie,delta)
    param_arg_keyword(1,2,3) #Will pass keyword delta=4 regardless
    param_arg_keyword(1,2,3,7) #Will pass 7 instead of delta=4
#param_arg_keyword_func()

def args_argument_func():
    def args_argument(alpha,bravo,*args,**kwargs): #Can call them something other than *args (Tuple),**kwargs (Dict)
        print(alpha,bravo)
        for arguments in args: #Calls Tuple, new lines
            print(arguments)
        for key_value in kwargs: #Calls Dictionary, values
            print(key_value,kwargs[key_value])
    args_argument(1,2,3,4,5, six=6, seven=7)
    args_argument(1,2, six=6, seven=7)
#args_argument_func()

def args_argument_func_2():
    def args_argument(alpha,bravo,*,charlie,delta): #Everything after * is keyword
        print(alpha,bravo,charlie,delta)
    args_argument(1,2,charlie=3,delta=4)
#args_argument_func_2()

def element_iter_for():
    numbers=[1,2,3,4,5]
    for i in numbers:
        print(i)
#element_iter_for()

#Mapping & Filtering
#Process & Transform items in iterable table w/o using explicit for loop
#Two arguments, 1st function, 2nd my list

def mapping():
    #Temperatures in celsius
    cels_temps = [("US", 50), ("Africa", 70), ("Australia", 90), ("Haiti", 50)]
    
    #Celsius to fahrenheit conversion via Lambda
    cels_to_fahr = lambda data: (data[0], (9/5)*data[1]+32)

    #Map function to iterate thru cels temperatures
    print("Mapping cels to fahranheit:", list(map(cels_to_fahr,cels_temps)))

#mapping()



#Filtering filters out unneeded data
def filtering():
    import statistics
    random_data=[1.3,2.7,0.8,4.1,4.3,-0.1]
    average=statistics.mean(random_data)
    print("Average of data:", average)

    #Select values above average
    filter(lambda x:x>average,random_data)
    print("Filter for above average:", list(filter(lambda x:x>average,random_data)))

    #Select values below average
    print("Filter for below average:", list(filter(lambda x:x<average,random_data)))

#filtering()

#Removing empty elements, careful as 0, 0.0 would be removed, as can be significant
def filtering_countries():
    countries=["","Argentina","Brazil","","Chili","","Venezuela"]
    print("Removing empty elements w/ filtering:", list(filter(None,countries)))

#filtering_countries()

#Python states use functools.reduce() in place of this, as for loop more readable
def reduce_function():
    from functools import reduce

    #Multiply all numbers in a list
    data=[2,3,5,7,11,13,17,19.23,29]
    multiplier=lambda x,y:x*y
    print("Reduce function:", reduce(multiplier,data))

    product=1
    for x in data:
        product *= x
    print("For loop instead of reduce:", product)

#reduce_function()


def my_generator():
    yield 1
    yield 2, 3

    #Only calls 1st yield
    value=next(my_generator())
    print(value)

    #Another required for 2nd yield
    value=next(my_generator())
    print(value)

#my_generator()

#Collections Module


#Generators# 1 at a time and only when asked, memory efficient w large data sets, yeild


#Fibbonachi Sequence
def fib():
    a, b = 0, 1
    while True:            # First iteration:
        yield a            # yield 0 to start with and then
        a, b = b, a + b    # a will now be 1, and b will also be 1, (0 + 1)

        for index, fibonacci_number in zip(range(10), fib()): #Indent back twice to run
            print('{i:3}: {f:3}'.format(i=index, f=fibonacci_number))

def even_vs_odds():
    num=0
    while (num<=12):
        if num%2==0:
            print("The number " + str(num) + " is even!")
        else:
            print("The number " + str(num) + " is odd!")
        num+=1
#even_vs_odds()

#Multiprocessing
def multiprocessing():
    from multiprocessing import Process
    import os
    import time

    def square_numbers():
        for i in range(100):
            i*i
            time.sleep(0.1)

    processes = []
    num_processes = os.cpu_count()

    #Create processes
    for i in range(num_processes):
        proc = Process(target=square_numbers)
        processes.append(proc)

    #Start
    for proc in processes:
        proc.start()
    
    #Join
    for proc in processes:
        proc.join() #Wait for process to finish, locked main thread

    print("end main") #Will only reach this point once 

#Multithreading
def multithreading():
    from threading import Thread
    import time

    def square_numbers():
        for i in range(100):
            i*i
            time.sleep(0.1)

    threads = []
    num_threads = 10

    #Create threads
    for i in range(num_threads):
        thread = Thread(target=square_numbers)
        threads.append(thread)

    #Start
    for thread in threads:
        thread.start()
    
    #Join
    for thread in threads:
        thread.join() #Wait for process to finish, locked main thread

    print("end main") #Will only reach this point once 








database_value = 0

#def increase(lock): ####Prevent Race condition with LOCK Paremeter and lock variable below
#    global database_value #Accesses global variable
#
#    with lock:
#        #Dont need this if using with lock: lock.acquire() ####Everytime lock acquired, needs release, state is locked, can modify value w/o switching back, 2nd thread can run thru this
#        local_copy = database_value
#        time.sleep(0.1)
#        database_value = local_copy
        #Don't need this if using with lock: lock.release() ####Everytime lock acquired, needs release

#if __name__ == "__main__":
  
#    lock = Lock() ######Prevent race condition with LOCK value
#    print("start value", database_value) #Start

#    thread1 = Thread(target=increase, args=(lock,)) ####Tuple, so needs comma to prevent race condition
#    thread2 = Thread(target=increase, args=(lock,)) ####Tuple, so needs comma to prevent race condition

#    thread1.start()
#    thread2.start()

#    thread1.join()
#    thread2.join()

#    print("end value", database_value) #end
#     print ("end main")

def queue_get():
    if __name__ == "__main__":

        que = Queue()

        que.put(1)
        que.put(2)
        que.put(3)

        #3, 2, 1 --> Front
        first = que.get()
        second = que.get()
        third = que.get()

        print("First in queue:", first)
        print("First in queue:", second)
        print("Third in queue:", third)

        #que.join() #Blocks until all in queue processed
        que.task_done() #Always need this is using que.get()

        sys.exit()
#queue_get()

def num_squared_try_except():
    try:
        num_square=input("Please enter a number to square: ")
        num_square=int(num_square)
        print("Your squared number is: ", num_square**2)
    except(ValueError):
        print("Please only enter a number")
    def accept_string():
        #try:
    
        print_string=input("Please enter a string: ")
        print_string=str(print_string)
        #except(something)
        print("Here is your string: " + print_string)
    accept_string()
    def opt_and_not_params(v,w,x,y=1,z=2):
        print("This is 3 params w 2 optionals", v+w+x+y*z)
    opt_and_not_params(1,2,3)
#num_squared_try_except()

def guess_language():
    languages=["C","C++","Python","Ruby"]
    guess=input("Guess a language: ")
    if guess in languages:
        print("Your language is in there!")
    else:
        print("Try again!")

#guess_language()

def z_is_5():
    def f(x):
        return x+2

    z=f(3)
    if z==5:
        print("z is 5")
    else:
        print("z is not 5")
#z_is_5()

def x_is_opt():
    def x_is_opt(x=2):
        return x**x
    print(x_is_opt())
    print(x_is_opt(4))
#x_is_opt()


def rhymes():
    rhymes = {"1": "fun",
          "2": "blue",
          "3": "me",
          "4": "floor",
          "5": "live"
          }


    n = input("Type a number:")
    if n in rhymes:
        rhyme = rhymes[n]
        print(rhymes)
    else:
        print("Not found.")
rhymes()

#def worker(que,lock): ###Will need lock parameter to prevent duplicate threads from appearing
#    while True:
#        value = que.get() #Will get first value
        #Processing..
#        with lock: ###Need lock here to prevent duplicate threads from accessing
#            print(f'in {current_thread().name} got {value}')
#        que.task_done()

#if __name__ == "__main__":

#        que = Queue()
#        lock=Lock()
#        num_threads = 10

#        for i in range(num_threads):
#            thread = Thread(target=worker, args=(que,lock))
#            thread.daemon=True ##Background thread exits when main thread exits, DEFAULT False, without it process will continue
#            thread.start()

#        for i in range(1, 21):
#            que.put(i)

#        que.join()

#        sys.exit()

"""PROCESSES
#Process = Instance of a program (e.g. a Python Interpreter, FireFox, etc.)
#+ Can use multiple CPUs, Cores
#+ Separate memory Space -> Memory not shared between processes
#+ New Process stated independently from others
#+ Proceses are interruptable/killable
#+ One GIL (Global interpreter lock) for each Process -> Avoids GIL Limitation
#- Heavyweight, More Memory, Slower than starting thread, IPC (Interprocess Comm.) Complicated
#THREADS
#Threads = Entity within process that can be scheduled, process can spawn multiple threads
#+ All threads within process share same memory, Lightweight
#+ Thread is faster starting than Process
#+ Great of I/O-bound tasks
#- Limited by GIL, only one thread at a time
#- No effect for CPU-bound tasks
#- Not interruptable, killable
#- Careful with race conditions
#       Race conditions are when two threads try to modify same variable at same time
#GIL GLOBAL INTERPRETER LOCK
#A lock that allows only 1 thread at a time to execute in Python
#Needed in CPython because memory management is not thread-safe
#Avoid Multiprocessing, use different free-threaded Python Implementation (Jython, IronPython)
#Use Python as a wrapper for third-party libraries (C/C++) -> Numpy, scipy"""

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
#lambdaFunction()
#test_value(1)
#jsonTut()
#multiprocessing()
#ultithreading()

#import time
#start_time=time.time()
#a=1000000
#a=a*10000000000000000
##stop_time=time.time()
#print("Duration: {}".format(stop_time - start_time))
#print (f"Duration: {start_time - start_time}")


###ROBOT PROJECT###
#sudo apt-get install -y git python3-pip python3-smbus i2c-tools
#pip install git+https://github.com/orionrobots/Raspi_MotorHAT
#sudo raspi-config
#Interfacing Options > I2C > Enable
#Interfacing Options > SPI > Enable
#sudo reboot
#sudo i2cdetect -y 1 #Scans I2C bus 1 for devices attached to Pi
#Controller found at 0x6f