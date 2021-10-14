'''
-- Python has 3 main sequence classes: list, tuple, string.
-- All these support indexing, ie tuple[0], list[0], string[0] are valid commands
-- memory is stored in bits, generally we talk about bytes(=8bits)
-- computer assigns particular memory address to byte. Eg: byte#2144, byte#2167
-- computer's main memory (RAM) can be efficiently accessed.(ie: it is as easy to retrieve byte#987456 as it's to retrieve byte#123)
-- individual byte of memory can be stored or retrieved in O(1) time complexity
-- identifier : name given to a byte
-- A group of related variables can be stored in consecutive computer's memory addresses. This group is called Array.
-- Array = ordered sequence of individual characters
-- python stores every character in a space = 2 bytes (1 cell = 2 bytes)
-- all cells retrieve data in O(1) time, but characters stored in each cell may have different sizes,
   so they might have different time complexities.(which should not be the case)
-- solution to this is that, each cell in array contains an object, this object is same in all cells. hence each cell occupy same space
-- computer has all the alphabets and numbers and symbols stored at a place called "main-place"
-- the object then just refers to a value (in main-place) when called, and not stores the value in memory.
-- array instances (eg : list slicing), doesnt create a new variable in new memory address, it just refers to objects in list,
   which inturn refer to value in main-place. ie: list_1[0]----> doesnt create new variable called "list_1[0]".
'''

'''
Dynamic ARRAY:
-- computer doesn't assign new memory space to a list whenever a new item is added in it. It does it by concept of "memory jumps"
-- computer assigns total of say 64 bytes (32 empty places) to an array. we keep filling the array till 32 places. but when we add the
   33rd item, instead of assigning array space = 66 bytes (33 empty places), it assigns it a value of 128 bytes (2 X the original value)
   because it knows that we will add items in array in future, and continuously assigning and reassigning new memory locations whenever
   an item is added is very combursome
-- while transitioning from 64 bytes to 128 bytes, a new array is created, which fetches refer points to main-place from the old array.
-- once refer points are fetched, the new array's memory location points to the values, and old array's memory location are emptied.
-- now values can be added to new array.
'''
import ctypes
class DynamicArray(object): #creating a Dynamic array blueprint
    def __init__(self):
        self.num_items = 0 #total number of items in list initially
        self.size = 1 #default size of array
        self.array_ = self.make_array(self.size) #function to create new array of size = self.size 
    def __len__(self): #returns number of items in list (__len__ is a special python function which return length of object)
        return self.num_items #overwriting original __len__ function
    def __getitems__(self,k): #returns item at index k
        if not 0 <= k < self.num_items: #catching exception to avoid error
            return IndexError("k is out of bounds")
        return self.array_[k] #return item at index k by slicing
    def append(self,item): #to add item at the end of array
        if self.num_items == self.size: #resizing if all spaces of array filled
            self.resize_(self.size)
        self.array_[self.num_items] = item #adding item to the end of the array
        self.num_items += 1 #updating the number of items in the list
    def resize_(self,old_size):
        new_size = 2*old_size #defining size of the new array
        new_array = self.array_(new_size) #creating the new array based on the new size
        for item in range (self.n):
            new_array[item] = self.array_[item] #copying elements from old array to new array
        self.array_ = new_array #assigning the newly built array as the "array_" attribute of the class "DynamicArray"
        self.size = new_size #updating the size of array
    def make_array(self,size):
        return (size*ctypes.py_object)() #creates empty array of size = size attribute of class
arr = DynamicArray() #function call

'''
Amortized analysis:
-- concept: time saved by fast operations and time expended by slow operations add upto give an acceptable run time.
-- amortized cost per operation = 
'''

#reversing an array: starting from terminals exchanging values and coming towards the center
def reverseList(Array_, start, end):
    while start < end:
        Array_[start], Array_[end] = Array_[end], Array_[start]
        start += 1
        end -= 1
    return Array_

#Max and Min in the array: 
def func_minmax(array_):
    min_val = array_[0]
    max_val = array_[0]
    initial_index = 1
    for _ in range (len(array_)-1):
        if array_[initial_index] > max_val:
            max_val = array_[initial_index]
        if array_[initial_index] < min_val:
            min_val = array_[initial_index]
        initial_index += 1
    return min_val, max_val
list_1 = [1000, 11, 445, 1, 330, 3000, 444]
func_minmax(list_1)

#"K"th max and min element of an array:
def kminmax(array_:list, k):
    for _ in range (k-1):
        min_, max_ = func_minmax(array_)
        array_.remove(min_,max_)
    min_,max_ = func_minmax(array_)
    return min_,max_

#sort an array of 0s,1s and 2s:
'''
-- create 3 variables low=0, mid=0, high=last index value.
-- low is to track the last index of 0s.
-- mid is to track the last index of 1s.
-- high is to track the first index of 2s.
-- if value at index m is 1: dont do anything, but increment m by 1
-- if value at index m is 0: switch it with the value at index low and increment mid and low by 1
-- if value at index m is 2: switch it with value at index high and decrement high by 1
-- loop above till mid becomes more than high (in which case, there will be only 2s beyond index mid)
'''
def sort012(self,arr):
    low=0
    high=len(arr)-1
    mid=0
    while mid<=high: 
        if arr[mid]==0:
            arr[mid] , arr[low] = arr[low] , arr[mid]
            mid+=1
            low+=1
            
        elif arr[mid]==1:
             mid+=1
            
        else:
            arr[mid] , arr[high] = arr[high] , arr[mid]
            high-=1

#moving all negative numbers on one side of array:
def sort_numbers(arr):
    low = 0
    for num in range(len(arr)):
        if arr[num] < 0:
            arr[num], arr[low] = arr[low], arr[num]
            low += 1 
    return arr

# finding union of two arrays
def doUnion(self, a, n, b, m):
        return set(a + b)

#finding maximum contigous sum: #kadane's algorithm
def maxSubArraySum(self,a,size): 
           
        max_so_far = -9999999
        max_ending_here = 0 
        for i in range(0, len(a)-1): 
            max_ending_here = max_ending_here + a[i] #adding numbers in each successive loop
            if (max_so_far < max_ending_here): #if the sum we got in this loop is greater than the sum we got in previous loop
                max_so_far = max_ending_here  #we set the new max_sum as the sum we got in the loop, else we stick with previous sum
            if max_ending_here < 0:  #if the sum we got in the loop is negative, it will only reduce the sum in next loop,so we make it zero instead
                max_ending_here = 0   
        return max_so_far

#