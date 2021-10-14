def function_():
    pass # creating an empty function

def func1():
    print("statement1")
    print("statement2")
func1() #defining and calling a function

def greet_name(name, location): #example of "POSITIONAL ARGUMENTS". ie the position of paramenter and argument in the tuple matters alot.
    print(f"hello {name}, you are at {location}")
greet_name("abhishant", "chandigarh") #function with input
# "name", "location" are the parameter, and "abhishant", "chandigarh" is the argument
# 1st argument (abhishant) is stored in 1st parameter (name) and the 2nd argument in 2nd parameter

def func_11(age : int): #----------> now the value of age in function call must be an integer.
    pass 

def func_11(age : int)->bool: #----> now the output from this function is typecasted to boolean datatype
    pass

def greet_name(name, location):
    print(f"hello {name}, you are at {location}")
greet_name(location="chandigarh", name="abhishant") #this is an example of keyward arguments,
#here the position of parameters and arguments dont really matters

def func_1():
    j=3
    return j #code after return call is not executed. SO, also used to exit a function
output = func_1()
print(output) # function with an output

def function_1(a,b):
    """
    This function can do sum
    """
    return a+b #docstrings are used as summary of what the function does

def function_2(a,b):
    a+=2
    b+=1
    print(a+b)
    function_2(a,b) #recursion

'''
Global variable = is in the main program, is available to every function.
Local variable = is present inside a function, and is available to only that function, not to any other code element.
1st the function will look for a local variable, if not found then only it will look for a global variable.
local and global variables are only for functions, loops and conditional statements dont have this concept.
'''

def func_1():
    l=5
    print(l)
func_1() # ---------> 5 : local variable is defined in the function
# print(l) ----------> error because this is a global function and no global variable for l is defined

l=10
def func_1():
    l=5
    print(l)
func_1() #----------> 5 (chooses local variable over global variable)
print(l) #---------->10 (only global variable is available so no other choice)

l=10
def func_1():
    global l
    l=5
print(l) #----------> 5 ,local variable l=5 was converted into global variable l=5, 
# so now global functions like "print" can also access it

def function_a(some_param):
    print("this is function_a")
def function_b():
    print("this is function_b")
function_a(function_b) #passing a function as an argument of another function
#function_a = higher order function

#default parameter values:
def func_1(a=1, b=2, c=3):
    print(a+b+c)
#now when we call the function it is not compulsory to give arguments. We can give them values.......but not compulsory.
func_1()                # a valid function call
func_1(a=4, b=5, c=6)   # also a valid function call

'''
*args : unlimited positional arguments : whenever we give *args an argument, python stores that argument value in a variable "args"
*args are used when we dont know how much arguments will be provided when function is actually called. eg: sum of "n" numbers. 
'''
def sum_function(*num):
    sum_ = 0
    for item in num:
        sum_ += item
    return sum_
print(sum_function(1,2,3,4,5,6))
#this will also work for sum_function(1,2,3)

'''
**kwargs : unlimited keyword arguments : stores argument and value from function call as key-value pair in dictionary
'''
def tourist_place(**destination):
    var_1 = destination["chandigarh"]
    var_2 = destination["mohali"]
    var_3 = destination["panchkula"]
    print(var_1, var_2, var_3)
tourist_place(chandigarh="rock garden", mohali="stadium", panchkula="zoo")
# in above function call if we dont mention value of panchkula, ie: tourist_place(chandigarh="rock garden", mohali="stadium"),
# this will throw an error because function will not be able to assign a value to var_3 hence function would be incomplete.
# to avoid error, use: var = destination.get("chandigarh")

#Lambda functions / Anonymous Functions -------> one line function
minus = lambda x,y : x-y
minus(5,4) #------> 1
#above is same as:
def minus(x,y):
    return x-y

#using function as an attribute:
def func1():
    return "this is the result from function call"
func2 = func1() #----------> assigns func1 to func2 (now func2 has all the functionality as func1), and also runs func1
func2 = func1 #------------> assigns func1 to func2
func2() #------------------> runs the func2 (which is same as func1)
func3 = func2 #assign func2's content to func3
del func2 #deletes func2
func3() #func3 still runs even after func2 is deleted (because we have created func3 as a clone of func2 and func2 is no longer required for func3 to work properly)

#returning function as a result:
def funcret(num):
    if num == 0:
        return print
    else:
        return sum
ans = funcret(1)    
ans(2,3) #---------->5
ans = funcret(0)
ans(2,3) #---------->2,3

#passing function as an argument:
def function_(function123): #we dont use paranthesis when we use function as an argument
    function123(2,3)
function_(print) #---------->2,3
function_(sum) #------------>5