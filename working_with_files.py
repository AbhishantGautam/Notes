'''
-- "r" - open file for reading ----------------------------------> default mode
-- "w" - open file for writing
-- "x" - creates file if not exists
-- "a" - add content to the end of file
-- "t" - if file contains only text open in "t" mode ------------> default mode
-- "b" - use when file contsins binary data
-- "+" - read + write
-- text file : my name is abhishant
               today weather is good
-- binary file : my name is abhishant\ntoday weather is good
'''
f = open("functions.py", "rt") # f ---> file handle
for line in f:
    print(line, end="") #------->prints all the lines in file one by one
content = f.read() # transfers data from file handle to the variable called "content". whatever data is transfered to content is deleted from file handle
print(content) #----> prints all the contents in the file
content = f.read(3) #----> reads first 3 characters of file handle
content = f.read(3) #----> reads next 3 characters of file handle (as first 3 characters are already deleted from file handle)
f.close() #-----> you must close the file you opened, so the file is now available to other users also.

f = open("functions.py", "rt")
print(f.readline()) #----------> prints first line
print(f.readline()) #----------> prints second line
print(f.readline()) #----------> prints third line
f.close()

f = open("functions.py", "rt")
print(f.readlines()) #---------> creates a list with each line as a seperate list item
# To avoid \n in the list we obtain from readlines, write: data_1 = file2.read().splitlines() 

f = open("functions.py", "w") #----> opens the file if already there, and creates one if file with name="functions.py" was not found
f.write("the weather just became humid") #--> deletes whatever was written in the older version, and replaces with new text
f.close()

f = open("functions.py", "a")
f.write("the weather keeps changing constantly\n") #----> adds the new text at the end of the file.
a = f.write("new letters added to the file")
print(a) #------> returns the total number of letters appended at the end of the file
f.close()

f = open("functions.py", "r+") #allows us to work in both read and append mode
print(f.read()) #--------> reads the content of file
f.write("file ends here") #---> appends the text at the end of the file

f.tell() #--------> tells at which position our pointer is in the file.
f.seek(10) #------> assigns new position to the pointer.(new assigned position = 10)
f = open("functions.py", "rt")
print(f.readline()) #----------> prints first line
f.seek(0) #--------> brings pointer back to the original position
print(f.readline()) #----------> prints first line again

with open("my_file.txt") as file:
    contents = file.read()
    print(contents) # How to open and read a file

with open("my_file.txt", mode="w") as file:
    file.write("New text") # How to open and edit a file

with open("my_file.txt", mode="a") as file:
    file.write("\n New text") 

'''
-- A table can be created by using CSV data(comma seperated values) 
-- it looks like: a, b, c
                  d, e, f
                  g, h, i
'''

with open ("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data) # converts all elements in all rows as a list. ie data = [[a,b,c], [d,e,f], [g,h,i]]
# To avoid \n in the list we obtain from readlines, write: data_1 = file2.read().splitlines() 

#more efficient way to use csv file is:
import csv
with open("weather_data.csv") as data_files:
    data = csv.reader(data_files) #----> creates a table with multiple rows
for row in data:
    print(row) #-----> prints each row

#most efficient way: use Pandas library
#pip install pandas
import pandas
data = pandas.read_csv("weather_data.csv")
print(data) #---->prints the whole table
#pandas creates an actual table with entries in first row as column title, and from 2nd row onwards the actual data.
print(data["temp"]) #---->prints all entries under the column "temp"
'''
-- pandas give output in form of 2 types of datastructures:
        1) Series(1-D): a single column (eg: data["temp"])
        2) Dataframes(2-D): whole table (eg: data)
-- pandas can convert Dataframes to various other datastructures like "dictionary", "excel form" etc
-- pandas can convert Series to other data structures like lists
'''
#extracting columns from table:
data_dict = data.to_dict() #creates a dictionary with row index as key and row items as value
temp_list = data["temp"].to_list() #creates a new list of all elements in the column "temp"
temperature_list = data.temp #a series will be created, data=object, temp=attribute (ie: pandas uses oop as its base concepts).

#extracting rows from table:
desired_row = data[data.day=="monday"] #shows all temperatures for monday

#extracting single item from table:
desired_row = data[data.day=="monday"]
desried_item = desired_row.temp

#create dataframe from dictionary:
data_dict={
    "student" : ["abhi", "shant", "gautam"],
    "scores" : [76, 77, 78]
}
data = pandas.DataFrame(data_dict)

#convert dataframe to csv file:
data.to_csv("new_data.csv") # new csv file("new_data.csv") will be created from the dataframe("data")
# This will automatically create an index column in the csv data. To avoid it we can do:
data.to_csv("new_data.csv", index=False) 

#looping through pandas dataframe:
for (index,row) in data.iterrows():
    if row.student == "abhi":
        print(row.scores)
        # we can also apply normal looping,but this type of looping is well optimized to work with pandas data.

#JSON

'''
-- JSON is widely used because it takes very less space for data storage
-- much like ikea, ikea dismantles a whole wardrobe into wooden planks and then ships it leading to minimum cost of transportation.
-- once the wardrobe reaches the customer, they construct back the wardrobe to its original form.
-- JSON : javascript object notation : stores data in the form of nested dictionaries 
   (may also include nested lists to give a key multiple values)
-- to view a json file in json format visit: jsonviewer.stack.hu
-- 3 major keywords:
    1) json.dump() -----> to write
    2)json.load() ------> to read
    3)json.update() ------> to update
-- is of the form:
    {"employees":[  
    {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},  
    {"name":"Bob", "email":"bob32@gmail.com"},  
    {"name":"Jai", "email":"jai87@gmail.com"}  
    ]}  
-- represents:
<employees>  
    <employee>  
        <name>Shyam</name>   
        <email>shyamjaiswal@gmail.com</email>  
    </employee>  
    <employee>  
        <name>Bob</name>   
        <email>bob32@gmail.com</email>  
    </employee>  
    <employee>  
        <name>Jai</name>   
        <email>jai87@gmail.com</email>  
    </employee>  
</employees>  
'''
import json
nested_dict_1 = {"employees":[  
    {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},  
    {"name":"Bob", "email":"bob32@gmail.com"},  
    {"name":"Jai", "email":"jai87@gmail.com"}  
]}  

#creating/writing a json file from a nested dictionary
new_data = {nested_dict_1}
with open("data.json", "w") as data_file: #"new_data" dictionary is stored in a variable called "data_file"
    json.dump(new_data, data_file) # "data_file" is linked with "data.json" (st: data_file and data.json have same content)
#for readability of json file, write: json.dump(new_data, data_file, indent=4)

#converting json file content into simple python dictionary
data = json.load(data_file) #stores json file content to variable called "data"
print(data)

'''
updating data in json file: (involves 3 steps)
    1)loading/reading the data currently in the json file.
    2)update/append the new data.
    3)dump/write the updated data in the original json file.
'''
with open("data.json", "r") as data_file:
    data = json.load(data_file) #read, step1
    data.update(new_data) #update, step2
with open("data.json", "w") as data_file:
    json.dump(data, data_file, indent=4) #writing, step3

'''
to convert csv data to list of key,value pairs(dictionary), ie:
column,row
a,1
b,2
c,3
to---
[{"column" : "a", "row" : 1},
 {"column" : "b", "row" : 2},
 {"column" : "c", "row" : 3}]
 we do:
'''
data = pandas.read_csv("data.csv")
to_learn = data.to_dict(orient="records")
print(to_learn)