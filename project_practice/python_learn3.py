##!!!REDO WEEK 4 READING&WRITING FILES WITH OPEN Python Data Science AI!!!###

import pandas
import sys
import matplotlib.pyplot as plt
import numpy as np
from collections import deque

#Local Variable first, then Global Variable if Local not available, unless "Global VARIABLE" defined in Function
#Synchronous = Single Thread, one operation runs at a time. (Slowest)
#Asynchronous = Multi-thread, operations run in parallel 
    #Multithreading = Operations run in parallel, but may block tasks, incur race conditions, memory contention
    #Multiprocessing = Multiple processes, each processor can run one or more threads, more resources than multithreading
    #Asyncio Fastest
def version():
    print(f"The following will input version: sys.version {sys.version}")
    
def data_structures1():
    #Sequences: Strings, Lists, Tuples
    #Stack = Linear DS LIFO Last In first Out #Append() = Add #Pop() = Remove Last Item
    stack_list=["Python","C++","Java","Ruby"]
    print(f"Stack list before .pop() method {stack_list}")
    stack_list.pop()
    print(f"Stack list after .pop() method {stack_list}")
    queue=[1,2,3,4,5]
    queue
    pass

def data_structures2():
    #Queue = Linear DS FIFO First First Out = from collections import dequeue #Append() = Add.  #Popleft() = Remove 
        #Uses = Keyboard buffers, Printer Queue, LinkedLists, PriorityQueues, Breadth-First searches
    #Priority Queues = FIFO serves higher priority elements first
        #Uses = Undo/Redo in text editors, Moving back/forward in browsing history, backtracking algs, calling functions
    my_queue = deque()
    print(f"my_queue = deque(): {my_queue}")
    my_queue.append(5)
    print(f"my_queue.append(5): {my_queue}")
    my_queue.append(10)
    my_queue.popleft()
    print(f"my_queue.append 10 and then .popleft: {my_queue}")
        
def variables_and_memory():
    #Variables begin with a-zA-Z or -. Variables cannot be numbers.
    #Variables stored in stack memory, Object or Value stored heap
    x=5
    y='a'
    print(x,"Variable X, stored in Stack, References 5, stored in Heap")
    id(x)
    print(id(x), "is Location of X in memory") #Print ID of X
    x=6
    print(id(x), "is location of X in memory after new value assigned") #Print ID of X

def methods():
    #Objects attached to variables
    name="Alpha"
    name_up=name.upper()
    name_low=name.lower()
    name_replace=name.replace("Alpha","Omega")
    name_find=name.find('lph') #Begin index of first letter found, if not found output is -1
    print(name_up,name_low,name_replace,name_find)

def data_types():
    #Integers, Floats, Booleans, Strings immutable, None
    #Type Casting converts
    #Aliasing (Copy by Reference) = Multiple names referring to same object i.e. a=[5,10] b=a. Same in memory 
    ##A side effect is if changing one, it will change other. Clone with b=a[:]
    c=int(5.5)
    d=str(7)
    test_string="This is a test"
    x, y = 5, 10
    z = 5.5
    a = True
    b = False
    n = None    

    print(f"Can split test_string 'This is a test' to list with test_string.split() {test_string.split()}")
    print(x,y, "This is Data Type integer X and Y")
    print("This is variable X which =", x, "the Data type is:", type(x))
    print("This is variable Z which =", z, "the Data Type is:", type(z))
    print("This is variable a which =", a, "the Data type is:", type(a))
    print("This is variable n which =", n, "the Data Type is:", type(n))
    print(f"C is a float, but casting as c=int(5.5) = {c}")
    print(f"D is a String, but casting as d=str(7) = {d}, and type(d) is {type(d)}")

def index_and_splicing_lists_tuples():
    #Sorted func returns new list, does not change. i.e. new_list_sorted=sorted(new_list) new variable
    #Sort method returns list in order, no new list new_list.sort()
    practice_list=['M','i','c','h','a','e','l'] #Lists = More Memory, Mutable
    practice_tuple=('M','i','c','h','a','e','l') #Tuples = Less Memory, Immutable. Lists in Tuples mutable, need comma, if just one element
    unsorted_tuple=(5,9,10,4,33,2,22,90)
    nested_tuple=("A",20,("Bore",30),("Cat",40), "D",60)
    print(practice_list[:3]) #Elements up to 3rd
    print(practice_list[::3]) #Every 3rd element
    print(f"Extending MULTIPLE elements practice_list.extend(['Pop',0]): {practice_list.extend(['Pop',0])}")
    print(f"Here is the new practice_list: {practice_list}")
    print(f"Appending SINGLE element practice_list.append('yahoo'): {practice_list.append('yahoo')}")
    print(f"Here is the new practice_list: {practice_list}")
    print(f"This is practice_list[0:5:2]: {practice_list[0:5:2]}") #Every 2nd element up to 5
    print(f"Can modify M with practice_list[0]='J'")
    practice_list[0]="J"
    print(practice_list)
    print(f"Can delete J with del(practice_list[0]")
    del(practice_list[0])
    print(practice_list)
    print("This will find first index of 'A': nested_tuple.index('A')")
    print(nested_tuple.index('A'))
    print(practice_tuple[0])
    print(len(practice_tuple))
    print(unsorted_tuple)
    print(f"This is a sorted tuple using sorted(variable) {sorted(unsorted_tuple)}")
    print(f"This is a nested tuple {nested_tuple}")
    print(f"Accessing nested_tuple[2][1] will be 30: {nested_tuple[2][1]}")
    print(f"Accessing nested_tuple[2][0][2] will be r: {nested_tuple[2][0][2]}")

def list_comprehension_data_structure():
    #Shorter way to write for statements
    compre_list=["A","B","C","D"]
    new_compre_list=[element for element in compre_list]
    print(new_compre_list)


def dictionaries(): #Key:Value pair #Keys immutable, unique #Values can be mutable, duplicates
    
    #Create variables and add them to dictionary
    variables_one=1
    variables_two=2000
    test_dict_two={}
    test_dict_two['variables_one']=variables_one
    test_dict_two["variables_two"]=variables_two
    print(f"Added test_dict_two['variables_one']=variables_one {test_dict_two}")

    test_dict={"Alpha":1,"Bravo":[2,3,3],"Charlie":3, ("TupleDelta"):(5,4)}
    print(f"Print test_dict: {test_dict}")
    print(f"Print first value using key test_dict['Alpha']: {test_dict['Alpha']}")
    print(f"Print next value using key test_dict['Bravo']: {test_dict['Bravo']}")
    print(f"Can access Value by Key test_dict['TupleDelta'] {test_dict[('TupleDelta')]}")
    
    #Add key/value with dict['KEY']='VALUE'
    test_dict['Delta']=4 #Adding Key Value pair
    print(test_dict)
    
    #Delete entry with del(dict['KEY'])
    print("Now will remove a key with del(test_dict['Alpha'])")
    del(test_dict['Alpha'])
    print(test_dict)

    print(f"Check all keys with test_dict.keys() and all values with test_dict.values() {test_dict.keys()} {test_dict.values()}")
    
    #Needs quotes' ' " " to check if Key or Value in dictionary
    print(f"Can check if 'value' exists with VALUE in test_dict: {'value' in test_dict}")
    print(f"Can check if 'key' exists with KEY in test_dict: {'Delta' in test_dict}")
    
    #Print all items with .items function
    print(f"Can check all key value pairs with .items() method test_dict.items {test_dict.items()}")

def sets(): #Venn Diagram, Collection like lists, tuples. #Unordered, no element recording #Unique elements #Duplicates not present
    set_one={"Alpha","Bravo","Charlie", "Charlie", "Bravo", "Delta"}
    set_two={"Alpha", "Bravo", "Omega", "Zeta"}
    set_three=set_one&set_two
    print(f"Adding set_three=set_one & set_two will output only elements in both sets {set_three}")
    print(f"Also use .intersection method to find in both sets set_one.intersection(set_two) {set_one.intersection(set_two)}")
    print(f"Union method with set_one.union(set_two) outputs all elements {set_one.union(set_two)}")
    print(f"issuperset method to verify if variable is superset set_one.issuperset(set_three) {set_one.issuperset(set_three)}")
    print(f"issubset method to verify if variable is subset set_three.issubset(set_one) {set_three.issubset(set_one)}")
    print(f"Find difference (elements in set1, not set2 or intersection) set_one with set_one.difference(set_two) {set_one.difference(set_two)}")
    print(set_one)
    print(f"Deleting all elements in set with set_one.clear() {set_one.clear()}")

    list_to_set=set(["Hummer","Tank","Helicopter","Plane","Bomber"])
    print(f"Using variable=set(['element1','element2']) will convert to set {list_to_set}")

    #Converting List to Set aka Type Casting
    list_one=["1","2","3","3"]
    print(f"Printing list_one which contains, 1, 2, 3, 3: {list_one}")
    list_one_set=set(list_one)
    print(f"Now printing same list converted to set with list_one_set=set(list_one): {list_one_set}")

    print(f"Adding value method to set with set_one.add('Value') {set_one.add('Value')} {set_one}")
    print(f"Removing value method from set with set_one.remove('Value) {set_one.remove('Value')} {set_one}")
    print(f"Verify if element in set with 'Value' in set_one {'Value' in set_one}")

def inputFunction():
    #print("Enter a name:")
    #inputNameString = str(input())
    #print("The name you entered is:", inputNameString)

    #print("Enter a whole number:")
    #inputInteger = int(input())
    #print("The integer you entered:", inputInteger)

    #print("Enter any integer:")
    #inputFloat = float(input())
    #print("The integer you input was:", inputFloat)

    print("The print function has sep=' ' and end='\\n' by default; change by adding sep=''")
    print ("Test","This","Out",sep='')
    print("Test","This","Out","again",sep=',')
    print("Test", "This", "Out", "again", "again", sep='\n')
    print("This will eliminate new line ",end='')
    print("Testing","Again")
    str1="Hey"
    str2="There"
    print(str1,str2,sep='')

    concatStrings=str1+str2
    print(concatStrings)

def operators_expressions():
    #Operator is +, -, /, %, *, //, **
    #Operand is the object.
    #Comparison Operator is ==, !=, <, >, <=, >=
    #Assignment operator is =, -=, += /=, +=
    #Logical Operator is AND, OR, NOT
    #If/else statements also considered 'Branching'
    #In Operator (Membership), Is Operator
        #Is validates if objects in same memory location
    #Expression is Operand + Operator
    a, b = 5, 7
    print("The floor divison of b / a, 7 / b:", b // a) #Floor of division
    print("The power of b**a, 7**5", b**a) #Power of
    name="Artificial"
    if "R" in name or "t" in name:
        print("Is R or t in Artificial, the name variable?:", True)
    else:
        print(False)

    t=20
    s=20
    print("The memory location of variable t = ", id(t), "The memory location of variable s = ", id(s))
    if t is s:
        print("Is t same memory location of s?:", True)
    else:
        print(False)
 
def sphereVolume(r):
    pi = 22/7
    Vol = (4 * pi * r ** 3) / 3
    return round(Vol, 2)

    r = 3
    Vol = sphereVolume(r)
    print("The volume of the sphere with radius", r, "is:", Vol)

def control_flow_statements():
    #if else, elif conditions
    #max,min in list, performs lexicographically if string
    print("Please input an age:")
    age=int(input())

    if age >=18:
        if age >= 65:
            print("The age is too old")
        else:
            ("This age is granted access")
    else:
        print("This age is too young")

    print("Please provide a number")
    num=int(input())
    if num>0:
        print("Positive")
    elif num == 0:
        print("Zero")
    else:
        print("Negative")

    scoreList=[90,50,40,95,95,80]
    highest=scoreList[0] #Index 0
    for i in scoreList: #Check condition
        if i > highest: #Iterate through highest
            highest=i #i will become highest
    print("Iterating and assigning i = highest is:", highest)
    print("Alternatively, using max(list), the highest is:", max(scoreList))

def gradingSystem():
    print("Provide number received 1 - 100:")
    grade=int(input())
    if grade>=90 and grade <=100:
        print("Grade A")
    elif grade<90 and grade>=80:
        print("Grade B")
    elif grade<80 and grade>=70:
        print("Grade C")
    elif grade<70 and grade>=60:
        print("Grade D")
    elif grade<60:
        print("Grade F")
    else:
        print("Invalid")


def leapYear():
    #Leap year every 4 years
    A=400
    if A % 400 == 0:
        print("Leap Year")
    elif A % 4 == 0 and A % 100 != 0:
        print("Leap Year")
    else:
        print("Not Leap year")
    
def fizzBuzz():
    result = []
    A=16
    for i in range(1, A): #Iterate over the range of 1 up to hitting A (16)
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    print(result)


def loops_range_iteratio_enumerate():
    #Initialize, Condition, Update
    i=1
    while i <=6:
        print(i, end=' ',)
        i+=1

    print('\n')
    
    j=1
    while j<=10:
        print(j, end=' ')
        j+=1
    
    print('\n',"Only even numbers:")

    #Print only even numbers
    k=0
    while k<=10:
        if k%2==0:
            print(k, end=' ')
        k+=1
    
    print('\n',"Only Odd Numbers:")
    k=0
    #Print only odd numbers
    while k<=10:
        if k%2==1:
            print(k, end=' ')
        k+=1

    print('\n')

    print("Sum of all numbers from 1 - 10:")
    m,add=1,0
    while m<=10:
        add+=m
        print(add,end=' ')
        m+=1
    print("Total is:", add)

    #Range(Start,End,Jump) just prints range
    ranger=range(5)

    #List prints elements
    list_range=list(range(5))
    list_range_back=list(range(10,0,-1))
    print(ranger)
    print(list_range)
    print(list_range_back)

    #For Loop = Iterator, Iterable, and Iteration
    #For Iterator, in Iterable: Iterate
    print("Enter a number to multiply by: ")
    num=int(input("> "))
    for i in range(1,11):
        print(i*num, end=' ')



    squares=["red","yellow","green"]
    
    #i = index, square = element
    for index,element in enumerate(squares):
        print (i,element)
    
def for_animals(): #List of animals whose names are made of 7 letters
    Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
    New = []
    i=0
    while i<len(Animals):
        j=Animals[i]
        if(len(j)==7):
            New.append(j)
        i=i+1
    print(New)


def print_rows_columns():
    for i in range(2): #Rows
        for j in range(4): #Columns
            print("#", end=' ')
        print()

    print("\nSelect number of rows to print: ")
    num=int(input("> "))

    for i in range(1,num+1):
        for j in range(i):
            print("#", end=" ")
        print()

def break_continue_pass():
    #Pass = No Op, Skips Synatx Error ||| Continue Skips ||| Break breaks out of loop
    for i in range (1,10):
        if i == 5:
            continue
        print(i, end=" ")

    print("\n")

    for i in range (1,10):
        if i == 5:
            break
        print(i, end= " ")

    print("\n")
    i=1
    while i<10:
        if i==5:
            break
        print(i)
        i+=1
    
def prime_number_finder():    
    print("Please enter a number to identify if Prime")
    num=int(input("> "))

    if num <= 1:
        print("False")
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            print("False")
        print("True")

def convert_temperature():
    celcius_to_fahrenheit = lambda celcius: (celcius * 9/5) + 32 
    fahrenheit_to_celcius = lambda fahrenheit: (fahrenheit - 32) * 5/9

    celcius = float(input("Enter Celsius temperature: "))
    fahrenheit = celcius_to_fahrenheit(celcius)
    print(f"{celcius} C is {fahrenheit} F")
    
    fahrenheit = float(input("Enter Fahrenheit temperature: "))
    celcius = fahrenheit_to_celcius(fahrenheit)
    print(f"{fahrenheit} F is {celcius} C")
    print (fahrenheit, "F is",celcius, "C")
    
def convert_pixels():
    print("Enter width pixels: ")
    width=int(input("> "))
    print("Enter height pixels: ")
    height=int(input("> "))
    print("Is this grayscale? Y/N: ")
    try:
        grayscale=str(input("> "))
        if grayscale.lower()==["y" or "yes"]:
            print(f"The total pixel count is {width*height}")
        elif grayscale.lower()==["n" or "no"]:
            print(f"The total pixel count is {width*height*3}")
        else:
            print("Please enter if Grayscale")
    except ValueError:
        print("Please enter if Grayscale")

def convert_bytes():
    print("Please select conversion:\n")
    print("1. Bytes to Bits")
    print("2. Kilobytes to Bytes")
    print("3. Megabytes to Kilobytes")
    print("4. Gigabytes to Megabytes")
    print("5. Terabytes to Gigabytes")
    print("6. Petabytes to Terabytes")
    
    while True:
        try:
            selection=(int(input('> ')))
            if selection==1:
                print("Enter Bytes: ")
                bytes=int(input("> "))
                print(f"{bytes} Bytes is {bytes*8} bytes")
                break
            elif selection==2:
                print("Enter Kilobytes: ")
                kilobytes=int(input("> "))
                print(f"{kilobytes} Kilobytes is {kilobytes*1024} Bytes")
                break
            elif selection==3:
                print("Enter Megabytes: ")
                megabytes=int(input("> "))
                print(f"{megabytes} Megabytes is {megabytes*1024} Kilobytes")
                break
            elif selection==4:
                print("Enter Gigabytes: ")
                gigabytes=int(input("> "))
                print(f"{gigabytes} Megabytes is {gigabytes*1024} Kilobytes")
                break
            elif selection==5:
                print("Enter Gigabytes: ")
                terabytes=int(input("> "))
                print(f"{terabytes} Terabytes is {terabytes*1024} Kilobytes")
                break
            elif selection==6:
                print("Enter Petabytes: ")
                petabytes=int(input("> "))
                print(f"{petabytes} Petabytes is {petabytes*1024} Kilobytes")
                break
            else:
                print("Please enter a whole number")
                break
        except ValueError:
            print("\nPlease enter a valid option\n")
            break

def func_add_one(add_num):
    output=add_num+1
    return output

def func_add_previous(func_add_one):
    return func_add_one

#*parameter can pass multiple arguments
def func_packed_tuple(*names):
    for name in names:
        #Return name returns 1st
        #Return names returns all
        return name

def func_packed_dict(**args):
    for key in args:
        print(f"{key} : {args[key]}")
        
        #print(key) = keys in argument
        #print(args[key]) = values in argument
        #print(args) = all values in argument


def func_multiply(a,b):
    return a*b

def func_mean(num):
    return sum(num)/len(num)

def median(numbers):
    """
    This function returns median of the given list of numbers
    """
    numbers.sort()
   
    if len(numbers) % 2 == 0:
       median1 = numbers[len(numbers) // 2]
       median2 = numbers[len(numbers) // 2 - 1]
       mymedian = (median1 + median2) / 2
    else:
       mymedian = numbers[len(numbers) // 2]
    return mymedian

def func_square(a):
    return a**2

def func_cubed(a):
    return a**3

def default_argument(x=4):
    if x>5:
        print("Less than 5")
    else:
        print("Greater than 5")

def try_except_else_finally_openfile_errors():
    #ZeroDivisionError = Cannot divide by zero.
    #NameError = Variable not defined
    #AttributeError = Attribute or method accessed on object that doesn't posess that attribute/method
    #KeyError = Key does not exist for dictionary
    #IndexError = Index does not exist for list
    #TypeError = Object used in incompatible manner, i.e trying to concat string and int.
    #ValueError = Inappropriate value used, i.e trying to convernt non-numeric to int.
    #Finally = Always executes, regardless of exception or not.
    try:
        openfile=open("myfile","r")
        openfile.write("My file for exception handling.")
    except IOError:
        print("Unable to open or read the data in the file.")
    else:
        print("The file was written successfully")
    finally:
        openfile.close()
        print("The file is now closed.")
    pass


def reading_files_open():
    #Readline() will read a single line
    #Readlines() will read all lines and return as a list of strings (Useful for loading in memory)
    #With statement is best practice when opening 'cause it auto closes
    #Modes = r, w, a(appending), r+ read and writes without truncating, w+ writes and reads and deletes all previous data.
    #r+ (with .truncate() method) and a+ useful for working with existing data
    #rb = read in binary format
    file_1=open("c:\\users\\artificial\\desktop\\Prompt.txt","r") 
    print(f"Printing file_1.name will show path to file: {file_1.name}")
    print(f"Print the file mode with file_1.mode: {file_1.mode}")
    file_content=file_1.read()
    print(f"Assign file_content = file_1.read(): {file_content}")
    line_1=file_1.readline() #Readline() will read a single line  
    line_2=file_1.readline() 
    print(f"Assigned line_1=file_1 and line_2=file_2: {line_1}{line_2}")
    file_1.close()
    print(f"Printing file_1.closed will print true or false if closed or not: {file_1.closed}")

    with open("c:\\users\\artificial\\desktop\\Prompt.txt","r") as file_1:
        all_lines=file_1.readlines() #Readlines() will read all lines and return as a list of strings (Useful for loading in memory)
        print(f"{all_lines}")
    print(f"Is file closed?: {file_1.closed}")
    
    with open("c:\\users\\artificial\\desktop\\Prompt.txt","r") as file_1:
        for line in file_1: 
            print(line) #Prints every line individually
    print(f"Is file closed?: {file_1.closed}")

    with open("c:\\users\\artificial\\desktop\\Prompt.txt","r") as file_1:
        print(f"{file_1.read(4)}") #Prints first 4 characters of text
    print(f"Is file closed?: {file_1.closed}")

    with open("c:\\users\\artificial\\desktop\\Prompt.txt","r") as file_1:
        i = 0
        for line in file_1:
            print(f"Iteration {str(i)} :  {line}")
            i = i + 1
    print(f"Is file closed?: {file_1.closed}")

    with open("c:\\users\\artificial\\desktop\\Prompt.txt","r+") as testwritefile:
        testwritefile.seek(0,0) #write at beginning of file
        testwritefile.write("Line 1" + "\n")
        testwritefile.write("Line 2" + "\n")
        testwritefile.write("Line 3" + "\n")
        testwritefile.write("Line 4" + "\n")
        testwritefile.write("Finished\n")
        testwritefile.seek(0,0)
        print(testwritefile.read())

def writing_files_open():
    #w to file erases previous data. a adds to file. w+ writes and reads and deletes all previous data (truncate)
    lines=["This is line C.\n", "This is line D.\n"] 

    with open("c:\\users\\artificial\\desktop\\Prompt2.txt","w") as file_1:
        file_1.write("This is line A.\n")
        file_1.write("This is line B.\n")

        for line in lines: ### 
            file_1.write(line)

    with open("c:\\users\\artificial\\desktop\\Prompt2.txt","a") as file_1:
        file_1.write("This is line E.")

    with open("c:\\users\\artificial\\desktop\\Prompt2.txt","r") as file_read:
        with open("c:\\users\\artificial\\desktop\\Prompt3.txt","w") as file_write: #Create new file, write
            for line in file_read: #For everything in file_read (Prompt2)
                file_write.write(line) #Write all lines to file_write (Prompt3)

    with open("c:\\users\\artificial\\desktop\\Prompt3.txt","r") as file_1:
        print(file_1.read())

    with open("c:\\users\\artificial\\desktop\\Prompt3.txt","a+") as file_1:
        print("Initial Location: {}".format(file_1.tell())) #Tell shows current position in bytes

        data = file_1.read()
        if (not data): 
            print("Read nothing")
        else:
            print(file_1.read())

        file_1.seek(0,0) #Seek (offset,from) method moves to specified bytes from beginning.

        print("New location: {}".format(file_1.tell()))
        data = file_1.read()
        if (not data): 
            print("Read nothing")
        else:
            print(data)
        print("Location after read:".format(file_1.tell()))

        with open("c:\\users\\artificial\\desktop\\Prompt3.txt","r+") as file_1: #Adding .truncate() will reduce file to data and delete all that follows 
            file_1.seek(0,0)
            print(file_1.tell())

def copying_files():
    with open(r"C:\Users\Artificial\Desktop\Newfile.txt") as source_f:
        with open(r"C:\Users\Artificial\Desktop|NewDestfile.txt") as destination_f:
            for line in source_f:
                destination_f.write(line)
    pass

def pandas_files():
    #DataFrames is two-dimensional data structure, rows and columns
    #Series is one-dimensional array of indexed data. Can get column of DataFrame as Series
    csv_path="c:\\users\artificial\\desktop\\file1.csv"
    data_frame=pandas.read_csv(csv_path)
    data_frame.head() #.head() method shows first five rows

    xlsx_path="c:\\users\artificial\\desktop\\file1.xlsx"
    data_frame2=pandas.read_excel(xlsx_path)
    data_frame2.head()

    songs={"Album": ["Great Cold Distance","Discouraged Ones"], #Can pass dictionaries to pandas
           "Released":[2006,1998],
           "Length":["1:00:00","2:00:00"]}
    

def pandas_uniques():
    csv_path="c:\\users\artificial\\desktop\\file1.csv"
    data_frame=pandas.read_csv(csv_path)
    data_frame["Album"].unique()

    data_frame_new=data_frame[data_frame["Released"]>=2000]
    data_frame_new.to_csv("newer_songs.csv")

def pandas_practice():
    x = {'Name': ['Rose','John', 'Jane', 'Mary'], 
         'ID': [1, 2, 3, 4], 
         'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
         'Salary':[100000, 80000, 50000, 60000]}
    data_frame=pandas.DataFrame(x)
    #print(data_frame)
    x=data_frame[["ID"]]
    z=data_frame[["Department","Salary","ID"]]
    y=data_frame["Name"]
    filtered_df=data_frame[(data_frame["ID"] > 2) & (data_frame["Salary"] < 80000)]
    print(filtered_df)
    print(f"Reassigning value of X: {x} which is data type {type(x)}")
    print(f"Assigning value of z=data_frame[[dept,salary,id]]: {z}")
    print(f"Assigning SERIES value of y=data_frame['Name'] which uses one bracket: {y} {type(y)}")
    print(f"")

async def pandas_loc_iloc():
    #loc() is a label-based data selecting method, pass row or column to select, last element of range
    ##loc(rowlabel,columnlabel)
    ##loc(0:2,'Name':'Department') will select rows 0,1,2 and columns Name thru and Department
    #iloc() is an index-based method, pass integer index to select specific row/column, not last element of range
    ##iloc(rowindex,columnindex)
    ##iloc(0:2,0:3) will select rows 0,1, and select columns 0,1,2
    ##set_index() method removes Index, moves header
    #.head() method shows first 5 rows
    x = {'Name': ['Rose','John', 'Jane', 'Mary'], 
         'ID': [1, 2, 3, 4], 
         'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
         'Salary':[100000, 80000, 50000, 60000]}
    data_frame=pandas.DataFrame(x)
    print(data_frame.iloc[0,0])
    print(data_frame.iloc[0,2])
    print(data_frame.loc[0,"Salary"])
    
    data_frame_2=data_frame
    data_frame_2.set_index("Name")
    print(data_frame_2)
    data_frame_2.set_index(["Name","ID","Department","Salary"])
    print(data_frame_2)
    print(data_frame_2.head())
    print(data_frame_2.iloc[0:2,0:2])
    print(data_frame_2.loc[1:2,"Name":"Department"])

class Circle (object): #Class Defined
    def __init__(self,radius=5,color='teal'): #Init = Constructor. Initializes attributes Self = Refers to newly created instance of class
        self.radius=radius
        self.color=color

    def add_radius(self,r): #Method
        self.radius=self.radius+r
        return (self.radius)
    
    def draw_circle(self): #Method
        plt.gca().add_patch(plt.Circle((0,0), self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()

class Rectangle(object):
    def __init__(self,height=5,width=4,color='red'):
        self.height=height
        self.width=width
        self.color=color

    def draw_rectangle(self):
        plt.gca().add_patch(plt.Rectangle((0,0),self.width,self.height,fc=self.color))
        plt.axis('scaled')
        plt.show()

class Vehicle(object):
    color='white' #Default color without ability to change in init
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
        self.seating_capacity=None #Allow seating capacity assignment

    def assign_seating_capacity(self,seating_capacity): #Allow seating capacity assignment
        self.seating_capacity=seating_capacity

    def display_properties(self):
        print("Properties of the vehicle:")
        print(f"Color: {self.color}")
        print(f"Max Speed: {self.max_speed}")
        print(f"Mileage: {self.mileage}")
        print(f"Seating Capacity: {self.seating_capacity}")


class Text_Analyser(object):
    def __init__(self,text):
        self.text=text
        format_text=text.replace('.','').replace('!','').replace('?','').replace(',','') #Remove punctuation
        format_text=format_text.lower() #Convert to lower case
        self.finished_text=format_text #Store converted text in new variable

    def frequency(self):
        word_list=self.finished_text.split(' ') #Splitting all words up
        freq_map={} #Empty dictionary
        for word in set(word_list): #Converting word_list to set(Unordered,No duplicates)
            freq_map[word] = word_list.count(word)
        return freq_map
    
    def frequency_of(self,word):
        freq_dict=self.frequency()
        if word in freq_dict:
            return freq_dict[word] #Return frequency of word
        else:
            return 0


def perform():
     a=np.array([1,1,1,1,1]) 
     return a+10
#print(perform())


if __name__ == "__main__":
    #version()
    #ariables_and_memory()
    #data_structures()
    #data_structures2()
    #data_types()
    #index_and_splicing_lists_tuples()
    #list_comprehension_data_structure()
    #methods()
    #dictionaries()
    #sets()
    #percentage_calculator()
    #inputFunction()
    #operators_expressions()
    #sphereVolume(5)
    #prime_number_finder()
    #control_flow_statements()
    #gradingSystem()
    #leapYear()
    #fizzBuzz()
    #convert_temperature()
    #loops_range_iteration()
    #print_rows_columns()
    #break_continue_pass()
    #convert_bytes()
    #convert_pixels()
    #reading_files_open()
    #writing_files_open()
    #copying_files()
    #pandas_files()
    #pandas_practice()
    #pandas_loc_iloc()

    ##Functions with Parameters
    #print(func_add_one(5))
    #print(func_add_previous(5))
    #print(func_packed_tuple("User_One","User_two"))
    #print(func_packed_tuple(["User_One",1],["User_two",2],["User_three",3]))
    #print(func_packed_tuple('One','Two','Three'))
    #print(func_packed_dict(Country="Canada",Province="Ontario",City="Toronto")) #Use = for key/value dict when passed as argument
    #print(func_multiply(2,12))
    #print(func_square(2))
    print(func_cubed(5))
    #default_argument()
    #default_argument(6)

    ##Classes
    '''
    print(dir(red_circle)) #List of object's methods
    teal_circle=Circle(radius=30) #Default parameter is teal, so no need to input color
    red_circle.add_radius(5)
    red_circle=Circle(10,'red') #Creating object instance
    red_circle.draw_circle() #Draw circle
    teal_circle.draw_circle()
    print(red_circle.color)
    print(red_circle.radius)
'''
'''
    thin_rectangle=Rectangle(5,4,'blue')
    thin_rectangle.draw_rectangle()
'''
'''
    first_vehicle=Vehicle(200,50000)
    first_vehicle.assign_seating_capacity(5)
    first_vehicle.display_properties()
    second_vehicle=Vehicle(180,75000)
    second_vehicle.assign_seating_capacity(4)
    second_vehicle.display_properties()
'''

'''
    provided_string="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."
    analyzed = Text_Analyser(provided_string)
    print(f"Formatted Text::: {analyzed.finished_text}") #Testing Lower Case works
    print(f"Frequency of all unique words: {analyzed.frequency()}") #Testing frequency of words

    word = 'lorem'
    frequency = analyzed.frequency_of(word)
    print(f"The word {word} appears {frequency} times.")
'''


###EFFICIENCY BigO Notation###
#O(1) = Constant, doesn't change
#O(n) = Linear, grows as data is added
#O(n^2) polynomial = Bubble sort
#O(x^n) exponential = 
#O(LogN) = Logarythmic, faster than linear
#O(NLogN) = Loglinear, most sorthing algorithms, slower than linear

#function decode (input):
#create output string ----> Only needs to happen once
#for each letter in input: ----> Only needs to happen once, can add before n
#get new_letter from letter's location in cipher ---> Needs to run for every letter in input
#add new_letter to output ---> Needs to run for every letter in input
#return output ----> Only needs to happen once

#Create and Return = O( 2)
#Get & Add New_Letter = 2n. This equates to O(2n+2). 2 is number of letters in input string
#If input string was 10 letters, it would be 2(10) + 2 or 22
#If input string was 1m letters, it would be 2(1mil) + 2 or 2mil
#For, Get, Add New_Letter = O(3n+2)
#Worst case for 26 letters, O((13+3)n+2) -> O(16n+2)
#Space Efficiency less frequently asked O(3n)

#Inserting/Copying in Array O(n)
#Searching Elements in Array O(1)

#Linked List, Next "Index" is Pointer to Memory
#Doubly Linked List Travels in both directions



#LIFO
#Stacks addition is Push O(1)
#Stacks removal is Pop O(1)

#FIFO
#Queues oldest is Head (Addition is Enqueue)
#Queues newest is Tail (Removal is Dequeue)

#2 Types of Queues
#Dequeus, Double Ended Queue, Goes both ways.
#Priority Queue