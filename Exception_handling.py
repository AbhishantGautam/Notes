'''
-- Exceptions : a way to catch and avoid errors.
-- keywords:
    1)try : something that might cause excepion
    2)except : do this if there was no exception
    3)else : do this if there were no exception
    4)finally : do this no matter what happens
'''
try:
    file = open("a_file.txt")
    a_dictionary = {"key" : "value"}
    print(a_dictionary["asdfghhgj"])
except FileNotFoundError: #if we dont mention type of error infront of except keyword, python will create exception for all errors.
    file = open("a_file.txt", "w")
    file.write("something")
except KeyError as error_message: #we can also pass the except block
    print(f"the key {error_message} doesnt exist") #stores error message in a variable
else: #executed if no error in try block
    content = file.read()
    print(content)
finally:
    file.close()

#we can also raise our customized error message:
height = float(input("height:"))
if height>=3:
    raise ValueError("you're overheight")

