'''
--Recursion consists of two parts:
    1. repeating case : n! = n*(n-1)!
    2. base case : 0! = 1
'''
def fibonacci(n):
    if n==0 or n==1: #base case
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2) #repeating case
        
#memoization : remembering result from a function call
#so that, if same arguments are reinputted, python doesnt re-run the whole function again and again. Rather returns the saved results
ef_cache = {}
def sq_number(num):
    if num in ef_cache:
        return ef_cache[num]
    result = num*num
    ef_cache[num] = result
    return result