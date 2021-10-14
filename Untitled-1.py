#install any python module using: pip install <ModuleName>==<version> (==<version> is optional)
'''
never name your python file as an existing python module. because when you type "import module", it will first look for the module
in the working directory, if you have a local file of the same name as module name, it will import the local file instead of the 
original module. 
'''
# Common Statements:
print("hello world")

print("my name is 'abhishant' gautam") 

print("hello world \n hello world") # Newline Character

print("Hello"+"world") # string concatenation

num = input("what is your number?") # Taking input
#always returns string value

print(len("abhishant"))
#always returns integer value
#length of number is not defined

print("Hello[0]") #string subscripting or slicing

# $4,65,89,100 -------> $4_65_89_100 (numeral seperation for easy reading)

str(123)
int(123.88)
float(123) #Typecasting

print(round(8.6)) #rounding off the number

print(8//3) #GINT operator

print(5%2) #Modulo operator (gives remainder when 5 is divided by 2)

abs(-11) #-------->11 (absolute function)

a=1
a += 1 
a -= 1
a *= a
a /= 2  #shorthand 

name_ = "abhishant"
print(f"hello {name_}") #f-string

final_text = "My name is {}".format("abhishant") #works like f-string

condition_1 = False
if condition_1 == True :
    print("the condition is True")
elif condition_1 == False :
    print("the condition is False")
else:
    print("please enter a valid value") #Conditional Statement
#You can use infinite amount of elif statements
#Even if one elif statement is true, python skips the rest of elif statements

condition_1 = False
if condition_1 == True :
    print("the condition is True")
if condition_1 == False :
    print("the condition is False")
if condition_1 == "something else":
    print("please enter a valid value") #Multiple if statements: used when every condition needs to be checked

name_="ABHIshant"
name_.lower() #changes all letters to lower case ----------->abhishant

name_.upper() #changes all letters to upper case ----------->ABHISHANT

name_.count("a") #returns number of times a letter occurs in a string ------------->2

name_.title() # returns --------> Abhishant

'''
comment_1
comment_2
comment_3
'''         # multiple line comment

print(
'''
print statement 1
print statement 2
print statement 3
'''
) # print multiple print statements

fruits = ["apple", "mango", "banana"]
for item in fruits:
    print(item) # most basic for loop

for num in range(1,10):
    print(num) # includes '1' but excludes'10'. ie: num values = 1,2,3.....,9
    #to include 10 also, we have to write: range(1,11)

for num in range(1,11,2):
    print(num) # the 3rd argument (ie 2), creates a step of 2, 
    #that means num assumes values from 1 to 10, but skips every alternate number (so num = 1,3,5,7,9)

condition_1=True
while condition_1:
    print("while loop is active")
    print("this may cause an infinte loop")

condition_1=False
while not condition_1: #we can also write "while condition_1 != True:"
    print("this is also a way to write while loop")

if "apple" in [fruits]:
    print("is present") # "in" keyword is used to check if a logic is TRUE or FALSE
    #here we checked if an item named "apple" was in the list. and the "in" condition returns true and if conditional is executed

fruit_string = "#".join(fruits) #concatenate all members of list and seperate them with "#". (ie it returns apple#mango#banana)

#mapping: (used to apply a function to all functions of array) | mapping function returns an object, so we need to typecast to list.
nums = [1,2,3,4,5,6]
nums = list(map(str,num)) #-----> ["1", "2", "3", "4", "5", "6"]
#good example:
def sq(n):
    return n*n
def cub(n):
    return n*n*n
func_list = [sq, cub]
for item in nums:
    val = list(map(lambda x:x(item), func_list))
    print(val) #--------> [1,1], [4,8], [9,27], [16,64], [25,125], [36,216]

#Filtering:
def greater_than_3(num):
    return num>3
greater_than_3_list = list(filter(greater_than_3, nums))
print(greater_than_3_list) #----------->[4,5,6]

#Reduce:
from functools import reduce
list_ = [1,2,3,4]
num = reduce(lambda x,y:x+y, list_) #-----> 10 ------> takes first 2 items in list and applies lambda function on it. 
#then takes the result and applies the lambda function on the result and 3rd item..then the result with 4th item and so on..


from turtle import * # imports everything from the turtle module

import random as randy # imports random module and names it "randy",
# now whenever we use this module, we write: num = randy.randint(1,10)

# To import modules not in python standard library : pip install <module name>, then import <module name>

test_list = [1,2,3]
if test_list: # or "if bool(test_list)"
    print("list is not empty")   # returns "list is not empty" if items are there in the list

var_1 = 56
if var_1: # or "if bool(var_1)"
    print("variable has some value") # returns "variable has some value" if var_1 was assigned a value.

#constants in python are always written in upper case, eg: CONSTT_VALUE = 25

'''
-- Absolute path : "C:\Users\abhis\# Random module.py" relative to the root directory
-- Relative path : "./project/talk.ppt" (in working folder look for folder called "project") ----> relative to working directory
                   "../work/project/talk.ppt" (in the previous folder look for a folder called "work")-> relative to working directory
-- In Python, ./ can be skipped for simplicity (ie "project/talk.ppt" will also look for folder called "project" in W.D)
-- ../../ is used to look in previous to previous folder
'''

sentence = "abhishant codes in python"
list_1 = sentence.split() #-------> creates a list containing individual alphabets in the sentence

#dynamic Typing in python: the datatype of a variable can simply changed by assigning it new values. Eg:
# 1) a="abhi" --------> datatype of a = str (a*2 is an invalid command)
# 2) a=2 -------------> datatype of a = int (a*2 is now a valid command)


#converting .py file to .exe file:
# in terminal : pip install pyinstaller
# pyinstaller <file name>.py
# this will create 2 folders "build", "dist" and a file called "main.spec"
# in the "/dist/main" folder you will get your .exe file.
# just zip your main file, and send it to the person you want to share your software with
# to only get one file that includes all of your

# Regular expression (REGEX):
import re
# major methods involved : findall, search, split, sub, finditer
# raw string : returns absolute value of the string. special characters are skipped. ie print(r"\n")----> \n, but print("\n") -> blank line
mystr = "lorem ipsum"
patt = re.compile(r"ph.no")
matches = patt.finditer(mystr)
for match in matches:
    print(match) #-----> prints the details of matched object----> returns wherever "ph.no" string is present in mystr
patt = re.compile(r".adm") #-----> returns all the information about string objects which include "adm" in it.
re.compile(r"^tata") #---------> string objects starting with tata
re.compile(r"tata$") #---------> string objects ending with tata 
re.compile(r"ai*") #---------> string objects containg 1 "a", and then, 0 to infinite number of "i"
re.compile(r"ai+") #---------> string objects containg 1 "a", and then, 1 to infinite number of "i"
re.compile(r"ai{2}") #---------> string objects containg 1 "a", and then, exactly 2 "i"
re.compile(r"(ai){2}") #---------> string objects containg exactly 2 "ai" #we grouped the string characters
re.compile(r"(ai){2}|t") #---------> string objects containg exactly 2 "ai" OR 1 "t"
# -- speacial sequence:
re.compile(r"\AFax") #------> returns match if "Fax" is at the beginning of any string object.
re.compile(r"\bFax") #------> returns match if "Fax" is at the beginning of any string objects.
re.compile(r"Fax\b") #------> returns match if "Fax" is at the end of any string objects.
re.compile(r"\d{5}-\d{4}") #-> returns match which contains 5 numbers, then a "-", then 4 numbers again.(\d --> digit numbers) 


#pickling:

# -- we can store any python object for later use(just like a pickle). That object need not belong to the same file we're working on.
import pickle
cars = ["audi", "bmw", "maruti suzuki", "porsche"]
file = "mycar.pkl"
fileobj = open(file, "wb")
pickle.dump(cars, fileobj)
fileobj.close() 
# this creates a pickle of cars list object. First we created a pickle file called mycar.pkl, then opened it as a file object as method = "wb"
# then we took the object we want to pickle (ie cars), and then dumped it into the file object.

#using the pickle: (on a seperate project)
file = "mycar.pkl"
fileobj = open(file, "rb")
mycar = pickle.load(fileobj)
print(mycar)


#Coroutines
# -- used to run a specific part of function first, but whenever the next time function is called, it starts from a certain checkpoint
#    so that the whole function is not rerun every time we call it. this saves time and reduces load on cpu.
def searcher ():
    import time
    book = "this is a book on harry potter which was written by jk rowling and is based on magic"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("your text is in the book")
        else:
            print("text is not in the book")
search = searcher() #function run first time
next(search) # runs the ongoing function till it is haulted (in this case interuppted to take user input)
search.send("harry") #this time it doesnt start from beginning, but continues from last chechpoint, and continues till haulted again
input("press any key") #haulted again
search.send("potter") # this time also function doesnt start from beginning, but continues from last checkpoint
search.close() #closes the coroutine

#Function Cacheing:
import time
from functools import lru_cache
@lru_cache(maxsize=3) #saves the returned value from my last 3 function calls.
def some_work(n):
    time.sleep(4)
    return(n)
if __name__ == "__main__":
    print("now running some work") #--- runs immediately because function run after this.. not before
    some_work(3)
    print("done...calling again") # --- takes 3 seconds to run, because this is the time taken by function to finish work
    some_work(3)
    print("called again") # --- immediately responds as the result from last function call was saved in cache.

#Generators
# iterable - python object that has a method __iter__() or __getitem__() already defined (these when run, provides an iterator)
# iterator - python object that has a method __next__()
# iteration - process of iterating
# iterable is any object across in which we can traverse through all of its items. for example: list, string, tuple etc. iteration is only possible in iterables.
# the __iter__() function provides an iterator to the iterable, which has the method __next__(), which provides next values for iteration
# generator: that iterator, in which we can traverse only once
# generator returns an object, and makes use of the keyword yield to provide result of function.
# yield keyword only presents 1 result at a time. Eg:
list_1 = [1,2,3]
def square_num(list_input): #generator
    for n in list_input:
        yield n*n
yielded_object = square_num(list_1) # creates an object which returns yield value of function for each subsequent function run.
next(yielded_object) # (1) --->runs the function for the first value in list and stops after returning the first result and for the next() command
next(yielded_object) # (4) --->runs the function again and returns the result and again wait for the "next()" command
next(yielded_object) # (9) --->runs the function again and returns the result and again wait for the "next()" command
next(yielded_object) # StopIterationError as no more values left to iterate
# now we dont have a way to restart from first value in list. ie: we can only traverse through an iterable "once" by using generator
# we can again iterate through the list by creating a seperate object
yielded_object_2 = square_num(list_1)
for num in list_1:
    print(next(yielded_object_2)) # prints all the results at once
# major advantage of generator is that it doesnt take up memory of computer to store returned values.
# we can create a generator by list comprehension also, by:
yielded_object_3 = (n*n for n in list_1) #using paranthesis instead of square brackets.
print(list(yielded_object_3)) #----> returns all the values in a list

#Enumerate function:
l1 = ["a", "b", "c", "d", "e"] #{a:0, b:1, c:2, d:3, e:4}
for index,item in enumerate(l1): #-----> returns 2 values: the item for iteration and its index
    if index%2 == 0: 
        print(f"items at odd positions are {item}")

#__name__ function:
'''
-- __name__ is an attribute that belongs to the location the function is being run.
-- __name__ is "<file name>" if the function is being used from another file called "file name"
-- __name__ is "__main__" if the function is being used by the same file that defined it.
-- "if __name__ == __main__", returns FALSE if the functionality is being imported.
'''
'''
eg:
file1:
        print(__name__) ---------> __main__
file2: 
        import file1 ------------> file2
'''

#if __name__ == __main__ :
'''
-- assume you have a file called "file1.py", and in it you have 3 functions. Now you opened a new file called "file2.py" and 
    imported file1.py. Now when you use func_1 from file1 in file2, all the 3 functions will also run automatically. to avoid this,
    you can enclose func_2 and func_3 in a name==main capsule. Now when you import file1 in file2, and run func_1, only func_1 will run
    and everything inside name==main capsule will not run.
'''

# Decorators: code element that when added to a function increases its functionality
# these are functions that take in a primary function as an argument and modifies the returned value from that primary function.
def dec1(func1):
    def nowexec():
        print("executing now")
        func1()
        print("executed")
    return nowexec
def print_smth():
    print("my name is abhi")
print_smth() #prints: my name is abhi
print_smth = dec1(print_smth) #decorator(dec1) added to the original function(print_smth)
#above prints:      executing now
#                   my name is abhi
#                   executed
#another way of adding decorator to function is by:
@dec1
def print_sum(a,b):
    print(sum(a,b))
print_sum(2,5) #--------->executing now
#                         7
#                         executed

    






































