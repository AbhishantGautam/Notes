#-------------------------------------------------  INTRO  ------------------------------------------------------------------------------------#

'''
--object oriented programming : method of structuring a program by bundling related properties and behaviors into individual objects.
--with this we can visualize code elements as objects having some attributes and methods.
--we first create a blueprint of the objects we want, we call this blueprint as a "class".
-- class name should start with capital letter,and every subsequent word should also have first capital letter. eg: class ThisIsClassName
--This class has its own attributes and methods,
  and the new object which is an instance of this class will also have the same attributes and methods.
--Two objects created from same class are said to be "2 seperate instances" if the same class,
    and the way the two objects differ is called the "state" (ie: differences in attributes and methods)
'''
#main objectives of creating classes and objects is : 1) avoid repetative code blocks
#                                                     2) restrict certain functions to a selected objects only
#                                                     3) simplifying code by assigning attributes and methods to cerain pieces of code

#class name should follow UpperCaseCamelCase convention for naming a class

class UserInput:
    pass # creating an empty class

'''
-- to access attributes of object : var_1 = object.attribute
-- to change attribute value of object: object.attribute("new_value") -----> sets "attribute" of that "object" as "new_value"
-- to access methods of object : object.method() ----> can also take in arguments. eg: timmy.forward(100)
-- 
'''

user_1 = UserInput() #creating an object from class
user_2 = UserInput()
#user_1 and user_2 are equated to the same statement, one might think that then user_1 == user_2, but that's not true. user_1 and
# user_2 are different objects! (ie different instances of the same blueprint). and occupy different addresses on the memory.

user_1.id = "001"
user_1.name = "abhishant" # adding attributes to your object
user_1.__dict__  #---------> {id:"001", name:"abhishant"}
# __dict__ keyword returns a dictionary with all the attributes and their values linked to the object/class
user_1.ide = "vscode" #whenever such command is given, python will look if the object already has an attribute called "ide",if so,
    # python will just update the value of "ide". but if there is no attribute called "ide", python will simply 
    # create a new attribute for that object called "ide" and assign it that value

#---------------------------------------------  CONSTRUCTOR  FUNCTION  ----------------------------------------------------------------------------------------#

#constructor:
'''
above we saw that we can create attributes of an object or class by typing object.attribute=smth or class.attribute=smth.
but if there were large amount of attributes, it would be very combursome to write new lines for each attribute.
here is where constructor comes in. we can define attributes of a class in its definition itself.
-- the constructor function will executed exactly at the time the object is instantiated. object wont even create until and unless
    the arguments in the constructor function are provided.
'''
class testclass:
    def __init__(self, num1, num2, num3):
        self.var1 = num1  #instance variable
        self.var2 = num2
        self.var3 = num3
    class_var = 4      #class variable
#whatever is written under the __init__ function, will be executed exactly at the time the object is first instantiated.
#  the variables in the__init__ function are a property of the object only. "testclass" will not have any attribute called "var1"
new_obj = testclass(num1=1,num2=2,num3=3)

'''
-- we can have a default value for objects created from a particular class.
-- This is done by using constructors and the __init__ keyword.
-- Everything written in the __init__ function call will be executed when an object is being made from that class.
'''
# class variable: variable defined in the class definition
# object variable: variable either inherited from parent class or unique variable created for object like: object.var_1=something

#self keyword:
class testclass1:
    testvar = 1 #class variable
    def testfunc1(self):
        return self.name
obj_1 = testclass1()
obj_1.testfunc1() #----->wherever self is mentioned in the function, python replaces it with "obj_1"--->similar to "obj_1.testfunc(obj_1)"

class Car:
    def __init__(self, seats, id): #setting attributes of class
        self.seats = seats
        self.id = id
        self.is_available = False # we have set a default value for the attribute "is_available" which doesnt depend on user input.
my_car = Car(5, 225) #-----> same as my_car.seats = 5 and my_car.id = 225

class Car:
    def enter_race_model(self):
        self.seats = 2
audi = Car()
audi.seats #--------> 2  (attribute can be accessed from the object)
Car.seats #---------> 2  (attribute can also be accessed from the class)
audi.seats = 4 # this will only change the value of "seats" of object "audi" and not change the value of class variable
Car.seats = 5 # this will change the value of class variable
# we cant change class variables just by making changes to its object variable*

'''
we can change the class variable in a way..but it is not generally preffered to change class variables from objects.
This is done by a decorator called "classmethods"
'''
class Car:
    seats = 2
    @classmethod
    def change_seats(cls, new_seats):
        cls.seats=new_seats
octavia = Car()
octavia.change_seats(4)
Car.seats #---------> 4

# classmethod decorator as a constructor:
class Car:
    def __init__(self,num1, num2) -> None:
        self.seats = int(num1)
        self.milaege = int(num2)
    @classmethod
    def from_str(cls,string):
        params = string.split("-")
        return cls(params[0],params[1],params[2])
obj_2 = Car.from_str("2-65") #---------------------->creates an object even when the input to constructor is in string-only format
obj_2.milaege #---------->65

#static method : class method which doesnt take "self" or "cls" as an argument, and is just a normal function provided to the object by class
class Car:
    def __init__(self,num1, num2) -> None:
        self.seats = int(num1)
        self.milaege = int(num2)
    @staticmethod
    def testfunction(): #static method : more efficient than normal class method
        return "this is just a test function"
obj_3 = Car()
print(obj_3.testfunction()) #-------> this is just a test function


'''
-- class inheritance : new class can inherit some attributes and methods from preexisting class.
-- the new class has some unique features and some features from its parent class
-- we can also over-write class method and class variables(aka instance variables)
'''
#instance variable is always given a higher priority than the class variable.
class TV:
    model = 200
    def __init__(self) -> None:
        self.model = 100
samsung = TV()
samsung.model #------> 100

#important priority:
class testclass:
    var_1 = 1 #------------------------------------(1)
    def __init__(self) -> None:
        var_1 = 2 #--------------------------------(2)
class testchild(testclass):
    var_1 = 3 #class variable ---------------------(3)
    def __init__(self) -> None:
        var_1 = 4 #instance variable --------------(4)
obj = testchild()
obj.var_1 #when looking for var_1's value, python will first look if there is an instance variable in testchild,if there is,it'll print that
#if there is no such variable, it will look for instance variable in the parent class, if it is there, it'll print that..else, it will
#look for a class variable in testchild, if it is there it will return that, else it will look for a class variable in parent class.
# therefore priority of var_1 will be : 4 > 2 > 3 > 1(least preffered) {not really look at the over-riding block right below}
# * instance variables are given higher priority than class variables

#over-riding constructor function : 
# in the above example we have over-ridden the constructor function (as well as the class variable) of the parent class.
# so now python will behave as if the constructor function and the class variable of the parent class doesnt exist.
# Therefore the above priority will be : 4 > 3 (because python assumes (1) and (2) dont exist)
#but what if we dont want to over-ride it blatantly,instead there was an instance variable called "special" without which program will crumble.
#for that we have super() function.

#super() function : function that returns the parent class. with this function we can access every method and attribute of parent class. Even its costructor function
class testclass:
    var_ = 1 
    def __init__(self) -> None:
        var_1 = 2 
class testchild(testclass):
    def __init__(self) -> None:
        var_1 = 4 #var_1 setted as 4
        super().__init__(self) #now the parents class's __init__ function is called, which sets the value of var_1 = 2
        var_2 = super().var_ #-------->
obj = testchild()
obj.var_1 #-----------> 2
obj.var_2 #----------->1

#the order in which we call the super function is also important. if in the above class we wrote:
class testclass:
    var_ = 1 
    def __init__(self) -> None:
        var_1 = 2 
class testchild(testclass):
    def __init__(self) -> None:
        super().__init__(self) #child class inherits its __init__ function from parent class. and setts var_1 = 2 -----------(cmd 1)
        var_1 = 4  #but here again var_1 was setted to 4 --------------------------------------------------------------------(cmd 2)
        var_2 = super().var_
obj = testchild()
obj.var_1 #--------> this will again give var_1 = 4 because (cmd 1) was over-ridden by (cmd 2)

class Animal:
    is_alive = True # class variable
    def __init__(self): # constructor
        self.num_eyes=2
    def breathe(self):
        print("inhale exhale")
class Fish(Animal): #Class Inheritance
    is_alive = False # instance variable (is_alive = False)
    old_alive = super().is_alive
    def __init__(self): # constructor method overwritten, now "self.num_eyes = 2" is not valid
        self.num_eyes = 3 #now "self.num_eyes = 3" is the valid statement
        super().__init__() # constructor method again inherited from parent class.
        #  above line now re-runs constructor method from parent class and "self.num_eyes = 2" is again valid.
    def swim(self):
        print("moving in water")
    def breathe(self):
        super().breathe()
        print("doing this under water")
# super() method lets us access overwritten methods from parent class from within child class (it does not accept any argument) 



# object insights:
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
skillf = Employee("Skill", "F")
# to get insights of various properties of objects we can do following:
print(skillf.fname) #prints the fname attribute of object
print(dir(skillf)) #------> returns all the methods and attributes available for that object
print(id(skillf)) #-------> returns the id of the objects (every object has its unique id)
print(type(skillf)) #-----> returns the datatype
import inspect
print(inspect.getmembers(skillf)) #----->returns alot of info
'''
hasattr()    :	It checks if an object has an attribute.
getattr()    :	It returns the contents of an attribute if there are some.
repr()       :	It returns the string representation of an object
vars()	     :  It checks all the instance variables of an object
issubclass() :	This function checks that if a specific class is a derived class of another class.
isinstance() :	It checks if an object is an instance of a specific class. 
__doc__	     :  This attribute gives some documentation about an object 
__name__     :	This attribute holds the name of the object
callable()   :	This function checks if an object is a function
help()       :	It checks what other functions do
'''
#---------------------------------------------  ABSTRACTION & ENCAPSULATION  ----------------------------------------------------------------------------------------#

#Abstraction : the process of breaking a big task into smaller components and each component providing some unique functionality.
#Abstracting something means to give names to things, so that the name captures the basic idea of what a function or a whole program does.
#To impliment abstraction, we require encapsulation
#Encapsulation : availing a functionality, not knowing how it was made possible.(using computer without knowing about RAM, hardrive,motherboard, etc)
#in encapsulation, we just provide the class, its attributes and its methods, and not care about the code in it.
# for example : class object, has attributes speed, health, coins. and has methods like "walk forward", "look left", "look right","turn around" etc
# we dont care about how the player walks forward or turns right... we should just know how to use the methods
# Encapsulation : hiding the implementation details

#encapsulation wraps the attributes and methods to single unit called object. This restricts the access to attributes and methods directly,
#and hence helps to avoid accidental modification of class's data. encapsulation works on the principle that
#"the object's important attributes should only be changed by object's own method only.". These important variables are called private variables

#----------------------------------------------  INHERITANCE  ---------------------------------------------------------------------------------------#

#Inheritance:
'''
-- Inheritance : procedure in which one class inherits the attributes and methods of parent class.
-- along with the inherited properties and methods, a child class can have its own properties and methods.
'''
class Car:
    def __init__(self, name, mileage):
        self.name = name 
        self.mileage = mileage 

    def description(self):                
        return f"The {self.name} car gives the mileage of {self.mileage}km/l"

class Audi(Car):
    def audi_desc(self):
        return "This is the description method of class Audi."

obj_4 = Audi("audi R8", 80 )
obj_4.description() #------------>The audi R8 car gives the mileage of 80km/l ----------->inherited method
obj_4.audi_desc() #-------------->This is the description method of class Audi.

# multiple inheritance:
class Car:
    def __init__(self, name, mileage):
        self.name = name 
        self.mileage = mileage 

    def description(self):                
        return f"The {self.name} car gives the mileage of {self.mileage}km/l"
class Truck:
    def __init__(self,name, mileage, weight) -> None:
        self.name = name
        self.mileage = mileage
        self.weight = weight
    def description(self):
        return "this is truck's description"
class omni(Car, Truck):
    is_spacious = True
    def print_des(self):
        return self.description
    def print_weight(self):
        return self.weight
    def print_space(self):
        return self.is_spacious
#this is how a new class can inherit from more than 1 parent class.
#in multiple inheritance, the order of inheritance matters alot. ie class omni(Car,Truck) and class omni(Truck, Car) are totally different
#whenever we try to access any method or attribute of the class "omni", it will first look into omni class's local class variables, if
#there is no such method or attribute, it will go look for it in the parent class first in the list, ie: Car in the first case, if it 
#still doesnt find the asked method or attribute then it'll look in the next parent class, and will keep repeating this until all the 
#parent classes have been checked. That is why order in which parent class is inherited is very important.
#Eg: class omni(Car, Truck, Bus), the priority goes like Omni > Car > Truck > Bus(least preffered).
#Even while constructing an object, object will look for the constructor function of its immediate parent class
#(ie obj = omni(*args) obj will look for an init function for omni class, there is no such constructor function, 
#then it will look for an init function in the Car class. There it finds one and hence it inherits the init function from there)
#information about init function is important because it will decide the number and type of input while object construction.
#ie if it inherits Car's init function, object construction will look like : obj = omni("omni lx", 80)
#if it inherits Truck's init function, object construction will look like : obj = omni("omni lx", 80, 1.5ton)


#Multilevel inheritance:
class Dad:
    def __init__(self, hobby) -> None:
        self.hobby = hobby
    def play_guitar(self):
        return "i play guitar"
class Son(Dad):
    def __init__(self, hobby) -> None:
        self.hobby = hobby
    def draw(self):
        return "i like to draw"
class Grandson(Son):
    def __init__(self, hobby) -> None:
        self.hobby = hobby
    def code(self):
        return "i like to code"
person_1 = Grandson("code")
person_1.hobby #-------->code
person_1.code() #-------> "i like to code"
person_1.draw() #-------> "i like to draw"
person_1.play_guitar() #----> "i play guitar"
#just like the multiple inheritance, when we call a method or attribute on an object, first it looks from the immediate parent class it 
# was constructed from (ie Grandson). If it fails to find any matching method or attribute, it goes to the parent class (ie Son) and if
#it still doesnt find any matching method or attribute, it will go the next parent class(ie Dad) like it did for person_1.play_guitar()

#Access Specifiers:
#public methods/attributes : open to anyone who uses our program. Written as self.hobby = hobby
#protected : open to the object's class and all the child classes of that class. Written as self._hobby = hobby
#private : open to only the object's class and nobody else. Written as self.__hobby = hobby
# private attributes are not accessible to anybody accept original class because, python cleverly doesnt save __hobby as just "hobby"..
# it saves it as "_Grandson__hobby" (this is called name mangling). so if we write "person_1._Grandson__hobby" we can access the private methods and attributes from anywhere

# good practise : create a getter and setter method for you protected and private attributes and methods:
class Robot:
    def __init__(self, name) -> None:
        self.__name = name
    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name
        return
terminator = Robot("terminator")
terminator.get_name() #------->shows the name of object
terminator.set_name("optimus") #----> changes the value of __name variable
#this practise helps us to change the attributes of a class by class's internal function. Hence avoids any outside attack

#-------------------------------------------  POLYMORPHISM  ------------------------------------------------------------------------------------------#

#polymorphism:
'''
-- "poly" means many, and "morph" means many forms.
-- polymorphism : the property of an object to have multiple forms.
'''
class bottle1:
    def __init__(self,color) -> None:
        self.volume = "250ml"
    def show_color(self):
        return self.color
class bottle2:
    def __init__(self,color) -> None:
        self.volume = "500ml"
    def show_color(self):
        return self.color
obj1 = bottle1("blue")
obj2 = bottle2("red")
obj1.show_color()
obj2.show_color()
#above show_color is a function that can have two forms depending upon which object it is being called upon

#poymorphism can also be seen in over-riding:
class bottle1:
    def __init__(self,color) -> None:
        self.volume = "250ml"
    def show_color(self):
        return self.color
class bottle3(bottle1):
    def show_color(self):
        return "this is the over-ridden show_color method"
obj3 = bottle3("blue")
obj3.show_color() #-----> "this is the over-ridden show_color method"
#but if there was no method called "show_color" in bottle3 class, the object will look for it in parent class, and return "blue"
#ie : the same function can return 2 different values depending on the availability of method in current class or one of its parent classes.

#polymorphism can also be seen when we input different type of variables in a function:
print(2+3) #------> 5
print("2" + "3") #-------->"23"

#-------------------------------------------  OVER-RIDING DUNDER METHODS  ------------------------------------------------------------------------------------------#

#Dunder Methods : function names starting and ending with double underscore "__". Eg: __int__, __dir__ etc
#these functions are performed exactly at the point an object is formed. 
# when we do a+b, python performs the function "add(a,b)". And in the background python runs the function __add__ which adds a and b
# however if we write : obj1 + obj2, python will get confused as __add__ function only takes integer inputs. this is called "operator overloading"
# However we can over-ride these methods also.
class bottle1:
    def __init__(self,volume) -> None:
        self.volume = volume
    def __add__(self,other):
        return f"{self.volume + other.volume}ml"
obj1 = bottle1(250)
obj2 = bottle1(750)
obj1+obj2 #---------------->1000ml
#the above __add__ method is modified only for the objects created from bottle1 class. 
#if we do 250+750 python will not return 1000ml. it will still follow the conventional __add__ method and return 1000.
#__repr__ method : tells details about an object
# __repr__ method over-riding 
class bottle1:
    def __init__(self,volume) -> None:
        self.volume = volume
    def __repr__(self) -> str:
        return f"This bottle has a volume of {self.volume}ml "
obj_ = bottle1(250)
print(obj_) #---------->This bottle has a volume of 250ml

#__str__ method : also returns object details. But is preffered over __repr__
class bottle1:
    def __init__(self,volume) -> None:
        self.volume = volume
    def __repr__(self) -> str:
        return f"This bottle has a volume of {self.volume}ml "
    def __str__(self) -> str:
        return f"This is the __str__ description of object with {self.volume}ml volume"
obj_ = bottle1(250)
print(str(obj_)) #-----> This is the __str__ description of object with 250ml volume
print(repr(obj_)) #----> This bottle has a volume of 250ml
print(obj_) #----------> This is the __str__ description of object with 250ml volume (__str__ method preffered over __repr__ method)
#however, if we didnt write the __str__ method, print(obj_) and even print(str(obj_)) would return "This bottle has a volume of 250ml"

#---------------------------------  ABSTRACT BASE CLASS & ABSTRACT METHOD DECORATOR  ----------------------------------------------------------------------------------------------#

#Abstract base class and @abstractmethod : a way for the parent class to pass instruction to its child class, about what all it should contain.
#for example if we want a rectangle class to always contain a print_area method, without which it should not have any permission to create objects,
#we can create a "shape" class which has an abstract method called print_area. when "rectangle" class inherits from it.it must contain the function "print_area"
#in return shape must inherit from class "ABC" to use this @abstractmethod decorator.
#imp : the shape class is not a normal class, rather it is an abstract class. NO OBJECT CAN BE CREATED FROM AN ABSTRACT CLASS.
#ie: obj_5 = shape() #not valid
from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def print_area(self):
        return 0
class Rectangle(shape):
    def __init__(self, length, breadth) -> None:
        self.length = length
        self.breadth = breadth
rect_1 = Rectangle(5,4) #----------> will throw an error. because the childclass of shape didnt contain the method "print_area"

class shape(ABC):
    @abstractmethod
    def print_area(self):
        return 0
class Rectangle(shape):
    def __init__(self, length, breadth) -> None:
        self.length = length
        self.breadth = breadth
    def print_area(self):
        return self.length * self.breadth
rect_1 = Rectangle(5,4) #----------> now this wont throw an error

#--------------------------------  PROPERTY DECORATOR AND SETTER METHOD  -----------------------------------------------------------------------------------------------------#

# @property decorator : used when we want to convert any "variable" to a "class attribute".
class Employee:
    def __init__(self, name) -> None:
        self.name = name
        self.email = f"{name}@gmail.com"
obj1 = Employee("abhi")
obj1.email #--->abhi@gmail.com
obj1.name = "shant"
obj1.email #---> this will still give abhi@gmail.com because we didnt change the value of email attribute. we only changed the name.

#we can solve this in 2 ways: 
class Employee:
    def __init__(self, name) -> None:
        self.name = name
        self.email = f"{name}@gmail.com"
    def set_email(self):
        self.email = f"{self.name}@gmail.com"
obj1 = Employee("abhi")
obj1.email #--->abhi@gmail.com
obj1.name = "shant"
obj1.set_email()
obj1.email #--->shant@gmail.com

#2nd way: above we needed to call a method to change the value of the email when name was changed.
#Instead, we just want to write obj1.set_email and that should return the newly set email, as if it was an attribute. so we use @property decorator
# @property decorator : converts a method into an attribute/property of the object.
class Employee:
    def __init__(self, name) -> None:
        self.name = name
    @property
    def set_email(self):
        return f"{self.name}@gmail.com"
obj1 = Employee("abhi")
obj1.set_email #---------->abhi@gmail.com
obj1.name = "shant"
obj1.set_email #---------->shant@gmail.com

#setter function
#once we create an attribute by @property decorator, we cannot change its property just by "obj1.set_email = gautam@gmail.com",we need 
#to create special setter function to change their values.
class Employee:
    def __init__(self, name) -> None:
        self.name = name
    @property
    def set_email(self):
        return f"{self.name}@gmail.com"
    @set_email.setter #sets new name
    def set_email(self,new_mail):
        self.name = new_mail.split("@")[0]
obj = Employee("abhi")
obj.set_email #-------->abhi@gmail.com
obj.name #------------->abhi
obj.set_email = "gautam@gmail.com"
obj.set_email #-------->gautam@gmail.com
obj.name #------------->gautam #changed the value of name from what we inputted for email
#setter function can also change the attribute from where our property was derived 
#(ie : we can also change the value of "name" based on the value we put for email)
#-------------------------------------------------------------------------------------------------------------------------------------#
