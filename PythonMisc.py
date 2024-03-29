import os
from threading import Thread, Lock, current_thread
import time
import sys
from queue import Queue
#Iterable = Python object with __iter__ or __getitem__ method defined returning iterator
#Iterator = Python object with __next__ or next method defined
#Iteration = Taking item from something like lists, the process itself


def fruit_list():
    define="#Lists"
    fruit_list=["Apple","Cherry"]
    print("My List:",fruit_list,define)

    fruit_list.append("Lemon")
    print(len(fruit_list))

    for i in fruit_list:
        print(i)

def my_tuple():
    my_tuple=tuple(["Max", 28, "SomethingHere"])
    print("My Tuple:", my_tuple, "#Tuples use () instead of [], faster, less memory")

def dictionary_one_n_two():
    define="#Dictionaries use {} or var=dict(key=\"value\")"
    dictionary_one=dict(name="Arti", age="27", city="city")
    print(dictionary_one, define)

    dictionary_one["email"]="somewhere@mail.com" #Adds "email": "mail.com" to dictionary
    print(dictionary_one, define)

    dictionary_alternate={"country":"US", "name":"Flarty"}
    print("Alternate way:", dictionary_alternate)

    dictionary_one.update(dictionary_alternate) #Merge dictionaryOne & dictionaryAlt
    print("Merging dictionary:", dictionary_one)

    if "name" in dictionary_one:
        print("If name in dictionary, print:", dictionary_one["name"])

    try: #Try/Except alternative to if statement
        print("Try/If statements alternate to if:",dictionary_one["name"]) 
    except:
        print("Error")

    for key in dictionary_one:
        print("If key in Dictionaryone, print key:", key)

    for key in dictionary_one.keys(): #Selects keys
        print(key)

    for value in dictionary_one.values(): #Selects values
        print(value)

    for key, value in dictionary_one.items(): #Selects both keys & values
        print(key, value)

def my_set():
    define="Sets are Unordered, Mutable, No Duplicates"
    my_set={1,2,3}
    print("My Set:", my_set,define)

    my_set_alternate=set([1,2,3])
    print("My Set Alternative:", my_set_alternate,define)

    my_set_odds={1,3,5}
    my_set_evens={2,4,6}
    my_set_primes={2,3,5}
    u=my_set_odds.union(my_set_evens) #Combines elements
    print("Union:", u,define) 

    intersect=my_set_odds.intersection(my_set_primes) #Combines like elements
    print("Intersection:", intersect,define) 

    diff=my_set_evens.difference(my_set_primes,my_set_odds) #Differences in elements
    print("Difference:", diff, define)

def read_file():
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

def write_file():
    employee_file=open(r'C:\Users\jslicker\Documents\Python\TestFile.txt', "a")
    employee_file.write("\nArti / Accounting") #Append to file
    employee_file.close()
    employee_file=open(r'C:\Users\jslicker\Documents\Python\TestFile.txt', "w")
    employee_file.write("\nArti -- Accounting") #Write new file
    employee_file.close()

def string():
    my_string="        Hello World"
    my_string=my_string.strip() #Removes whitespace
    print(my_string, "#Removing Whitespace with .strip() method")
    print(my_string.upper(), myString.lower(), "#Upper and Lower with upper(), lower() methods")
    print(my_string.endswith('Hello')) #Returns boolean value 
    print(my_string.find('o')) #Returns index -1 if character/substring not found
    print(my_string.count('p')) #How many characters in string
    print(my_string.replace('World', 'Universe')) #Replaces first word with second

    my_list=my_string.split(",") #Converts string to list
    print(my_list)

    new_string=''.join(myList) #Converts list back to string, preferred as cleaner & faster than 'for i in myList: myString+=i
    print(new_string, '\n')

    var="UsernameOne"
    var2="UsernameTwo"
    var3="NewVariable1"
    var4="NewVariable2"
    my_var="The variable is %s" % var #Old format
    print(my_var)
    var_num=3

    my_num="The variable is %d" % varNum #Old format
    print(my_num)
    var_float=5.512

    my_float="The variable is %.2f" % var_float #Old format, %.2f = two decimal places
    print(my_float)

    my_var="The variable is {} and {}".format(var,var2)#New Format, multiple variables with "{} and {}".format
    print(my_var)

    my_var=f"The variable is {var_float:.2f} and {var_float:.2f}" #f is New Format, fastest
    print(my_var, "#New Method")

    my_float="The variable is {:.2f}".format(var_float) #New Format, :.2f = two decimal places
    print(my_float)

def my_collections(): #Collections are containers that stores elements as dictionary keys and values
    from collections import Counter 
    a="aaaaaabbbbbbccccccdddd"
    my_counter=Counter(a)
    print("My Dictionary via Counter:", my_counter)
    print("My keys: ", my_counter.keys())
    print("My Values:", my_counter.values())
    print(my_counter.most_common(1))
    print("My list of elements: ", list(my_counter.elements()))

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

def iter_tools(): #Iterators data types in for loops like lists
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


#*Arg and **kwarg
def var_args(first_arg, *argv):
    print("First normal arg:", first_arg)
    for arg in argv:
        print("Another arg through *argv:", arg)

#var_args('One', 'Two', 'Three', 'Testy')





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

my_generator()

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

def increase(lock): ####Prevent Race condition with LOCK Paremeter and lock variable below
    global database_value #Accesses global variable

    with lock:
        #Dont need this if using with lock: lock.acquire() ####Everytime lock acquired, needs release, state is locked, can modify value w/o switching back, 2nd thread can run thru this
        local_copy = database_value
        local_copy += 1 #Increasing database value
        time.sleep(0.1)
        database_value = local_copy
        #Don't need this if using with lock: lock.release() ####Everytime lock acquired, needs release

if __name__ == "__main__":
  
    lock = Lock() ######Prevent race condition with LOCK value
    print("start value", database_value) #Start

    thread1 = Thread(target=increase, args=(lock,)) ####Tuple, so needs comma to prevent race condition
    thread2 = Thread(target=increase, args=(lock,)) ####Tuple, so needs comma to prevent race condition

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("end value", database_value) #end
    print ("end main")

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



def worker(que,lock): ###Will need lock parameter to prevent duplicate threads from appearing
    while True:
        value = que.get() #Will get first value
        #Processing..
        with lock: ###Need lock here to prevent duplicate threads from accessing
            print(f'in {current_thread().name} got {value}')
        que.task_done()

if __name__ == "__main__":

        que = Queue()
        lock=Lock()
        num_threads = 10

        for i in range(num_threads):
            thread = Thread(target=worker, args=(que,lock))
            thread.daemon=True ##Background thread exits when main thread exits, DEFAULT False, without it process will continue
            thread.start()

        for i in range(1, 21):
            que.put(i)

        que.join()

        sys.exit()

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
#my_collections()
#iter_tools()
#lambda_function()
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
