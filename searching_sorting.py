'''
--sequential search: we search item by individually matching it with each item in the data structure.
--sorted list: if a list is sorted, if a number greater than desired number is encountered, we dont need to check further
'''
def ordered_seq_search(arr,ele):
    pos = 0
    found = False
    stopped = False
    while pos <len(arr) and not found and not stopped:
        if arr[pos] == ele:
            found = True
        else:
            if arr[pos]>ele:
                stopped = True
            else:
                pos += 1
    return found

#Binary Search : starts searching from the middle of ordered list. if desired number > middle number, look for items after the middle number.
# else: look for items before the middle items
#this is called "divide and conquer"
def binary_search_iterative(arr,item):
    first = 0
    last = len(arr)-1
    found = False
    while first<=last and not found:
        mid = (first+last)/2
        if arr[mid] == item:
            found = True
        else:
            if item < arr[mid]:
                last = mid-1
            else:
                first = mid+1
    return found
def rec_bin_search(arr,item):
    if len(arr) == 0:
        return False
    else:
        mid = len(arr)/2
        if arr[mid] == item:
            return True
        else:
            if item > arr[mid]:
                return rec_bin_search(arr[mid+1:],item)
            else:
                return rec_bin_search(arr[:mid],item)

'''
-- Hashing : searching a data structure in O(1) time.
-- Hash table : collection of items, stored in such a way as to make them easy to find later
                each position of hash table is called slot, each slot can hold an item. and are named by integer value starting with 0
                initially hash table is empty
-- hash table is implemented using a list with each element initialized to "None"
-- relation between item and slot in hash table is called hash funciton
-- hash function takes item as input and return the slot name(integer)                
-- Remainder method(type of hash function) : h(item) = item % 11 (we're alotted 11 spaces of memory)
-- similarily we have folding-method and mid square method for integer values, and ordinal method for string values.
-- our goal while choosing hash function:
    1) minimize number of collision
    2) is easy to compute
    3) evenly distributes number, and doesnt waste unnecessary memory space
-- O(1) time searching: we take our target number, pass it through the hash function. 
        by this we get the hash value, which is also the value of index position. if there is a value in that index position,
        it will return true, else will return false. and this takes only one operation of checking if an index has some value or not. therefore O(1)
-- collision : two items with same hash value.
    solution-1) try to find another open slot for item that caused collision(rehashing), if it is filled, look for another slot, 
                and keep repeating until you get a vacant slot. This is called "Open Addressing".
    solution-2) assign to each slot a list of items that correspond to all the items whose hash values are equal to the slot name.    
'''
class HashTable(object):
    
    def __init__(self,size):
        
        # Set up size and slots and data
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size
        
    def put(self,key,data):
        #Note, we'll only use integer keys for ease of use with the Hash Function
        
        # Get the hash value
        hashvalue = self.hashfunction(key,len(self.slots))

        # If Slot is Empty
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        
        else:
            
            # If key already exists, replace old value
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  
            
            # Otherwise, find the next available slot
            else:
                
                nextslot = self.rehash(hashvalue,len(self.slots))
                
                # Get to the next slot
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))
                
                # Set new key, if NONE
                if self.slots[nextslot] == None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                    
                # Otherwise replace old value
                else:
                    self.data[nextslot] = data 

    def hashfunction(self,key,size):
        # Remainder Method
        return key%size

    def rehash(self,oldhash,size):
        # For finding next possible positions
        return (oldhash+1)%size
    
    
    def get(self,key):
        
        # Getting items given a key
        
        # Set up variables for our search
        startslot = self.hashfunction(key,len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot
        
        # Until we discern that its not empty or found (and haven't stopped yet)
        while self.slots[position] != None and not found and not stop:
            
            if self.slots[position] == key:
                found = True
                data = self.data[position]
                
            else:
                position=self.rehash(position,len(self.slots))
                if position == startslot:
                    
                    stop = True
        return data

    # Special Methods for use with Python indexing
    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)

'''
Sorting: process of rearranging data in a sequence
1) Bubble Sort : python makes multiple passes through the list, compare 2 adjacent items, and exchange if they are out of order.
                 each pass places the largest value infront of the list (ie: largest item bubbles to the top with each pass)
2) Selection Sort : python makes only one exchange per pass. python looks for the largest value as it passes through the list, and then replaces it with the item in the end
                    this requires n-1 passes to sort n items
3) Insertion Sort : python creates a new seperate list(with first item as the original list),
                    then it picks numbers one by one from the original list and start from right.
                    now it compares it with items in the new list and find the suitable position,
                    once it finds one, it inserts it there.
4) Shell Sort : modification of insertion sort in which, a group of items are first sorted and after that insertion sort is implemented on the list
5) Merge sort : --recursive algo that splits the list in half.
                --base case : list is empty or contains only 1 item
                --if more than one items, list is splitted in two, and merge sort is called on each of the splitted list recursively
                --once seperated to singular items, we sort them by grouping them together
'''
def bubble_sort(arr):
    for n in range(len(arr)-1,0,-1):
        for k in range(n):
            if arr[k]>arr[k+1]:
                arr[k],arr[k+1] = arr[k+1],arr[k]
    return arr

def selection_sort(arr):
    for fillslot in range(len(arr)-1,0,-1):
        position_of_max = 0
        for location in range(1,fillslot+1):
            if arr[location]>arr[position_of_max]:
                position_of_max = location
        arr[fillslot],arr[position_of_max] = arr[position_of_max],arr[fillslot]

def insertion_sort(arr):
    for i in range(1,len(arr)):
        current_value = arr[i]
        position = i
        while position>0 and arr[position-1]>current_value:
            arr[position] = arr[position-1]
            position = position-1
        arr[position] = current_value
    return arr

def shell_sort(arr):
    sublist_count = len(arr)/2
    while sublist_count > 0:
        for start in range(sublist_count):
            gap_insertion_sort(arr,start,sublist_count)
        sublist_count = sublist_count/2
def gap_insertion_sort(arr,start,gap):
    for i in range(start+gap,len(arr),gap):
        currentvalue = arr[i]
        position = i
        while position >= gap and arr[position-gap]>currentvalue:
            arr[position] = arr[position-gap]
            position = position-gap
        arr[position] = currentvalue