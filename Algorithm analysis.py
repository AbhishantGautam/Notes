#-------------------------------------------  TIME COMPLEXITY  ------------------------------------------------------------------------------------------#

'''
Big-O notation : describes how quickly runtime will grow relative to the input as input get arbitrarily large.

 -- name            BigO(time complexity)

    constant        1
    logarithmic     log(n)
    linear          n
    log-linear      nlog(n)
    quadratic       n^2
    cubic           n^3
    exponentially   2^n
-- constant, logarithmic, linear, log-linear --------> desired (lower the slope of "relative runtime vs n" slope, better the algorithm)
-- for small value of n, runtime is almost same for all algos
'''
list_1 = [1,2,3,4,5,6,7,8,9,10]

#constant: (undergoes only one operation no matter how big the list is)
def func_const(values):
    print (values[0])
func_const(list_1)

#linear: (undergoes one operation for every item in list)
def func_linear(values):
    for num in values:
        print(num)
func_linear(list_1)

#quadratic: (undergoes n operations for every item in lost)
def func_quad(values):
    for item in values:
        for num in values:
            print(item, num)
func_quad(list_1)

#when the value of "n" grows to large numbers, only the fastes growing terms matter and constants are dropped
# ie: for n-->infinity, O(n) ~ O(2n)

#complex function:
def comp_func(values):
    print(values[0]) # O(1)
    midpoint = (len(values)/2) # O(1)
    for item in values[0:midpoint]: # O(n/2)
        print (item)
    for num in range(10): # O(10)
        print('hello world')
comp_func(list_1)
# bigO = O(1 + 1 + n/2 + 10) = O(n/2 + 12) = O(n)
#ie : comp_func() has a time complexity of order "n" {linear}

#best and worst possible scenario:
def matcher(list, match):
    for item in list:
        if item == match:
            return True
    return False
matcher(list_1, 1) #------> best scenario, because complexity=O(1), ie: item == match in first go itself.
matcher(list_1, 11) #-----> worst scenario, because complexity=O(n), ie: no.of operations increase with no. of list items.
#                   (ie: item == match will not happen, but for that, python will run for loop for every item in list)

#whenever someone asks for BigO, assume the worst possible scenario.

#------------------------------------------  SPACE COMPLEXITY  -------------------------------------------------------------------------------------------#

'''
space complexity : how efficiently the function allocates memory when it is run
'''
#O(n) space complexity
def create_list(n):
    new_list = []
    for num in n:
        new_list.append("new")
    return new_list
create_list(5) # items in list increases as the value of "n" increases. therefore, linear space complexity

#O(n) time complexity, but O(1) space complexity:
def printer(n):
    for num in range(n):
        print("hello world")
printer(5) #function runtime increases with "n", but space complexity=O(1) as only one memory unit required to store "hello world"
#-------------------------------------------------------------------------------------------------------------------------------------#