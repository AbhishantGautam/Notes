#Data Structures
#-----------------------------------------------------------  LISTS  --------------------------------------------------------------------------#
#lists
'''
- datatype used to store multiple values
- the order is significant
- whenever you see [], just think of lists
- 
'''
list_1 = [1,2,3,"usa", "india"] #initiate the list

list_1[2] #returns item at the index 2 (ie 3) ---->list slicing

list_1[-2] #returns the item at index {len(list_1) - 2}

list_1[2] = 4 #changes item value at index position 2

list_1.append("pakistan") #adds a new item at the end of the list

list_1.remove("item name") #removes "item name" from list

list_1.extend(["sri lanka, bangladesh"]) #adds a list at the end of the list

names = "abhi shant gautam chandigarh"
names_list = names.split(" ") #creates a new list and appends element whenever a space is encountered

len(list_1) # returns the number of items in list

list_2 = [["abhi", "shant"], ["gautam", "chandigarh"]] #nesting lists

list_2[0][1] # returns item in the list at index 0 and inside that returns item in the nested list index 1 (ie "shant")

list_3 = [1,2,3,5,6,7]
sum_of_items = sum(list_3) #returns sum of every element in list
max_value = max(list_3) #returns maximum value among items in list
min_value = min(list_3) #returns minimum value

#list slicing
name = "abhishant"
name[0:4] #---------->abhi (slices characters at index 0,1,2,3)
name[0:400] #-------->abhishant (slices characters at index 0,1,....399. but only characters till index 8 are available)
name[:4] #----------->abhi (automatically starts from 0th index)
name[0:] #----------->abhishant (automatically goes till len(name))
name[:] #------------>abhishant (automatically starts from 0th index and goes till len(name))
name[0:9:2] #-------->ahsat (starts from 0 till 8th position and skips every 2nd number from beginning)
name[::-1] #--------->tnahsihba (slices characters from starting to end but at an interval of -1, ie: in reverse direction)
name[-4:-2] #-------->ha (starts from item at index -4 (ie h) and goes till index -3 (ie a) ie: excludes index -2nd position)

#list comprehension : new_list = ["operation" for "item" in "sequence"]------> creates list by looping, only in one line of code
num_list = [1, 2, 3, 4, 5, 6]
new_list = [n+1 for n in num_list] #---------->[2, 3, 4, 5, 6, 7]
#the sequence can be: list, range, string, tuple etc, the output from list comprehension is always a list.
#conditional list comprehension:
new_list = [n+1 for n in num_list if n>3] #--->[5, 6, 7]

#-----------------------------------------------------  DICTIONARY  --------------------------------------------------------------------------------#

# DICTIONARY
'''
Datatype which stores key, value pairs.
'''

dict_1 = {
    "first_name":"abhishant",
    "last_name":"gautam",
    "age":23,
    "location":"chandigarh",
} # initiating a dictionary

#extracting (key,value) pair from dictionary:
keys=[]
values=[]
for key,value in dict_1.items():
    keys.append(key)
    values.append(value)
#.items() keyword returns a tuple containing the key and the value pair from the dictionary

item_value = dict_1["first_name"] #getting the value of a key from dictionary
item_value = dict_1.get("first_name") #this will also return the value of key, but if value is not available, it wont throw an error.

dict_1["hobby"] = "coding" #adding items to dictionary

dict_1 = {} #deletes all entries in dictioanry

dict_1["first_name"] = "abhi" # edit / update an item in dictionary

for key_item in dict_1:
    print(key_item) #gives key
    print(dict_1[key_item]) #gives value

dict_1["location"] = ["chandigarh", "panchkula", "mohali"] #nesting a list in dictionary
# a key can have multiple values by this method

dict_1["first_name"] = {
    "name" : "abhishant",
    "house_name" : "abhi",
    "friends_call_me" : "gautam",
} #nesting a dictionary inside a dictionary

travel_log=[
    {
        "first_name" : "abhishant",
        "location" : "chandigarh"
    },
    {
        "first_name" : "gautam",
        "location" : "mohali"
    },
    {
        "first_name" : "anurag",
        "location" : "Bihar"
    }
] # this is a very common practise by nesting a dictionary inside a list.
#to get data: travel_log[1][first_name] ------> gautam

'''
dictionary comprehension:
1) {new_key : new_value for item in list}
2) {new_key : new_value for (key,value) in dict.items()}
3) {new_key : new_value for (key,value) in dict.items() if <conditional statement>}
'''

#------------------------------------------------  SETS  -------------------------------------------------------------------------------------#

#set
'''
-- used to store unique values
'''
set_1 = set([1,2,3,4])
set_1.add(2) #----> doesn't add 2 to set_1 because it already has it.
# it is represented as : {1,2,3,4}
#all the set operations like union, interation, disjoint etc are applicable in it.

#--------------------------------------------------  TUPLES  -----------------------------------------------------------------------------------#

#tuple
'''
-- used when we dont want our items to be changable
-- you also cant delete an item from tuple. you can delete the whole tuple if you want
'''
num = (1,2,3,4)
num[0] = 5 
print(num) #error:'tuple' object does not support item assignment
del(num) #deletes the tuple

#you can however change the values in tuple but that is not really what you want to do.
num = (1,2,3,4,5,6)
num[0] #---------> 1
num_list = list(num)
num_list[0] = 7
num = tuple(num_list)
num[0] #---------> 7
#-------------------------------------------------------------------------------------------------------------------------------------#