'''
-- framework : a huge library which along with the functionalities also provides the rules to use those functionalities in the best way possible
-- preinstalled files in django:
    1. manage.py : used to run server : dont change
    2. asgi.py, wsgi.py : dont change
    3. __init__.py : nothing in it
    4. settings.py : contains the project configurations
    5. urls.py : contains all the urls of the project

'''
# python -m pip install Django -------------> installs django framework
# django-admin startproject mypage ---------> creates a new django project
# python manage.py runserver ---------------> runs a local server (http://127.0.0.1:8000) {press ctrl+c to close the server}
# when we run server, a dummy database of the name "db.sqlite3" is created. This is the default database used by python
# python manage.py startapp challenges ------> starts a new app called challenges within the project
# every app has some premade files : migrations,init,admin,apps,models,tests and views.
# mypage.com/posts/python-blog => mypage.com is called the domain name
# views(function/class) : python code that runs when a specific url is searched. It handles the requests and sends the response
# major objective of views:
    # 1)load and prepare data
    # 2)run python logics
    # 3)prepare and return response data (eg: HTML)
from django.http import HttpResponse, response
def index(request):
    return HttpResponse("this works") #simplest view
#to tell django when to run a specific view, we need to link the view to specific url, this is done in the urls.py file.
#to build urls.py, we perform following steps:
# 1) in urls.py of the main project folder,write:
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path("challenges/", include("challenges.urls"))
]
# 2) create a urls.py in the app folder and in that write:
from django.urls import path
from . import views
urlpatterns = [
    path("january", views.index),
    path("february", views.index_feb)
]
#registering your code as one of the apps of your project: by default any new file that you create, python will treat it as a 
#seperate file. To make python know that the file that you created is indeed one of the apps, do:
    # 1) go to settings.py --> installed apps
    # 2) inside that list, add your app name, like: INSTALLED_APPS=['blogs',-----,----,---and so on]
#Http response not found error:
from django.http import HttpResponseNotFound
def my_view(request):
    if False:
        return HttpResponseNotFound("page not found")
#Dynamic url segments: used to give result refined for the user, depending the on the url they inputted. this is used when we dont
#know the url name before-hand, and for that we create a placeholder, whose values can be adjusted depending upon the url that is requested
urlpatterns=[
    path("<month>", views.monthly_challenge)
]
def monthly_challenge(request,month):
    challenge_text = None
    if month == "january":
        challenge_text = "Wake up early"
    else :
        challenge_text = "wake up late"
#Path converters : converts the data type of the dynamic segment to the desired datatype.
path("<int:month>", views.monthly_challenges)
#Redirects: used to redirect to another url when a certain url is searched. Eg: when we enter mypage/1 we want to be redirected to mypage/january
from django.http import HttpResponseRedirect
def monthly_challenge_by_number(request,month_num):
    if month_num == 1:
        redirect_month = "january"
    else:
        redirect_month = "february"
    return HttpResponseRedirect("/challenges/" + redirect_month)
#naming a url : (comes very handy)
urlpatterns = [
    path("<str:month>", views.monthly_challenges, name="month-challenge") #also see reverse function
]
#reverse function: used to construct a valid url, by assigning value to the dynamic segment
from django.shortcuts import redirect
from django.urls import reverse
def testview(request, month):
    redirect_path = reverse("month-challenge",args=[month]) #replaces the <str:month> placeholder with actual value to create a valid url
    return HttpResponseRedirect(redirect_path)
#Adding HTML files:
# 1) In app folder, create a folder called "templates". 
# 2) Inside "templates" create a new folder called "challenges", and inside that add your .html file
#you can not simply do : httpresponse("challenges/challenge.html").
#As python cant read an html file, we first need to convert html elements to string objects and then use python to read it
#render_to_string : function that converts an HTML file to a string datatype
def testView(request):
    from django.template.loader import render_to_string
    response_data = render_to_string("challenges/challenges.html")
    return HttpResponse(response_data)
#render : used to render html files withour converting them to string format
from django.shortcuts import render
def testView(request):
    return render(request, "challenges/challenge.html")
# render is also used to provide varible's value to the Django template language
#Dynamic Django Page: Standard HTML + Django Template Language
'''
-- Interpolations " {{}} " are django templates used to refer to a value of the variable in HTML file. {{num}} ----> 2
-- Interpolations have filters, that is we can use some functions on the variables. Eg: {{month|title}} ----> month.capitalize
-- Tags " {% %} " : used to run python code in an html file.
'''
def someview(request,challenge_text):
    return render(request, "challenges/challenge.html", {
        "text" : challenge_text
    })
#  <h2> {{text}} </h2> ------------->  use of interpolations in django

# <ul>
#     {% for month in months %}
#         <li> {{month}} </li>
#     {% endfor %}
# </ul>  ----> similarily we can do for conditional statements. -----------> use of tags
#url keyword: same as reverse, used to build valid urls by giving value to the dynamic segment, but this is used in html file.
# <a href="{% url'month-challenge'month %}">link to homepage </a>
#Template Inheritance: we can inherit our html file from a base html file and make improvements to it depending on the type of webpage we want
# 1) create a folder called "templates" at the same level as manage.py
# 2) inside it create a file called "base.html"
#to use the base template file, we need djano to acknowledge it as a valid template. do so by:
# 1)in settings.py ----> templates list 
# 2)under "DIRS" list, add : BASE_DIR/"templates"
# base.html file includes some dynamic elements which we can replace when building actual webpage from the base template.
# these dynamic elements are built with the help of block keyword inside tags.
# <head> ----------------------->parent
#     <title>{% block page_title %}challenge{% endblock %}</title> ["challenge" is the placeholder, s.t: if there is no code assigned to block page_title, "challenge" will be assigned to it]
# </head>
# <body>
#     {% block content %}{% endblock %}
# </body>
#{% extends "base.html" %} -----> child
    # {% block page_title %}
    # All challenges
    # {% endblock %}
#HTML snippets: HTML code snippets which we can "include" in other html files.
# 1)create a new folder(on the same level as the other html files you want snippet to use in) called "includes"
# 2)inside that create a "header.html" file
# <header> ----------------------------------->snippet
# <nav>
#     <a href="">all challenges</a>
# </nav>
# </header>
# {% block content %} ------------------------>html file which used the snippet
#     {% include "challenges/include/header.html" %}
# {% endblock %}
#we can also give value to a variable in the snippet when we use it in another html file by:
# {% include "header.html" with name = "abhishant" %}
#difference between django template language and python :
# python: dict_1["key"], func_1()
# dtl:    dict_1.key,    func_1 
#creating your custom 404 error page: ------------------------------------> works only when DEBUG = False
# 1) in the main templates folder, create a "404.html" file, and write:
# 2) {% extends "base.html" %}
#    {% block page_title %}something went wrong{% endblock %}
# 3) from django.http import Http404
    # try:
    #     pass
    # except:
    #     raise Http404()
#Adding static files (css,js,images):
# 1)inside app folder, create a new folder called "static"
# 2)inside it create another folder called "challenges"
# 3)inside that folder create a new file called "challenges.css"
# 4)in settings.py, in installed apps, check if "django.contrib,staticfiles" is there.
# 5)in index.html write:
    # {% extends "base.html" %}
    # {% load static %}
    # {% block css_files %}
    # <link rel="stylesheet" href="{% static "challenges/challenges.css" %}
    # <img src="{% static "blog/images/"|add:post.image %}" #add keyword used for concatenation in django template language
    # {% endblock}
#adding GLOBAL static files:
# 1) at the same level as manage.py create a new folder called "static"
# 2) inside that create a new file called "styles.css"
#by default when looking for static files django will check inside various apps for a file called "static"
#for our base static file to be noticed by django, in settings.py, under staticfiles_dirs list, append: BASE_DIR/"static"
#DATA is of 3 types:
    # 1)temporary:data is used immediately and lost thereafter. this data is stored in memory as variables. Eg: Userinput
    # 2)semi-persistant data:data is stored for a longer time, but maybe lost and can be recreated.
    #   Stored in browser,cookies,temporary files. Eg:user logged in status, user authentication status
    # 3)Persistant data:data is stored forever and must not be lost. it is stored in a database. Eg: blog posts, orders etc
#Django ORM(object relational mapping): Translates python code into SQL code and delivers to DBMS, intakes output by SQL and converts it into python object
#ORM is only for languages that support object oriented programming.
#there are two most popular ORM for python : SQLAlchemy and Django-ORM.
#ORMs make use of object managers to convert SQL data to python objects. for Django-ORM, it is done by the keyword "objects".
#Eg: student.objects.all()
#By default Django uses splite3 as the database. We can however transit to other DBMS like PostgreSQL or MySQL. 
#For this transition, we need an Adaptor(aka driver). In case of PostgreSQL it is "psychopg2"
#We can also use RAW SQL queries instead of ORM:
student = "some table in database"
posts = student.objects.raw("SELECT * FROM student_student")
#to create a table : 
from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
#once we create a table we need to add it to our database. We do this by making and running migrations.
# python manage.py makemigrations --------> gets the data that needs to be added to the database, and creates 0001_initial.py file in migrations folder of the app
# python manage.py migrate ---------------> adds data to database
#whenever we change the structure of table, we need to make migrations again
#inserting data:
# python manage.py shell
# from book_outlet.models import Book
# harry_potter = Book(title="harry potter", rating=5) #creates an object as an instance of table item
# harry_potter.save() #adds this object into the table
#retrieving data from database:
# Book.objects.all() ------> returns the data as data object with weird name like : <QuerySet[<Book:Book object(1)>,<Book:Book object(2)>]>
#to avoid this type of weird name, we can overwrite the __str__ method of objects:
from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
    def __str__(self) -> str:
        return f"{self.title}({self.rating})"
    #here we didnt change the table's structure, so we dont need to make migrations again.
#Validators: used to set limits to the entered values:
    from django.core.validators import MaxValueValidator,MinValueValidator
    rating = models.IntegerField(
        validators = [MinValueValidator(1), MaxValueValidator(5)]  # says that 1 < rating < 5
    )
#Adding more columns to the table:
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
    author = models.CharField(null=True, max_length=10)
    is_bestselling = models.BooleanField(default=False) #now makemigrations and migrate
#Updating data:
harry_potter = Book.objects.all()[0]
harry_potter.author = "J.K Rowling"
harry_potter.save()
#Deleting Data:
harry_potter = Book.objects.all()[0]
harry_potter.delete() #once we delete an entry, its id number is never reassigned to other new entries
#creating new entry to table:
Book.objects.create(title="Harry Potter 1", rating=5, author="Jk rowling", is_bestselling=True)
#get() keyword: returns only one value.
Book.objects.get(title="harry potter")
#if there were multiple books with title = harry potter, it would throw an error. Therefore, only use get method on "id" field only.
#to get all the books with title = "harry potter":
# Book.objects.filter(title="harry potter")
#filter() keyword : used to filter the dataset returned by the database.
'''
--Book.objects.filter(rating__lt=3) ---> books with ratings lower than 3
--Book.objects.filter(title__icontains="story") ---> returns the objects that contain story in it. it doesnt distinguish between story or sToRy.
--Book.objects.filter(title__contains="story") ----> same as icontains, but story and sToRy are not same.
from django.db.models import Q
--AND keyword(multiple conditions) : Book.objects.filter(rating__lt=3 AND title="harry potter")-----> Book.objects.filter(Q(rating__lt=3),Q(author="jk rowling"))
--OR keyword: Book.objects.filter(Q(rating__lt=3)|Q(author="JK.rowling"))
--Bulk operations: applying a function to multiple data sets:
    1) deleting many entries at once: Book.objects.filter(rating__lt=3).delete()
    2) updating many entries : Book.objects.all()[0].headline = "this is entry 1"
                               Book.objects.all()[1].headline = "this is entry 2"
                               Book.objects.all().bulk_update(objs,["headline"])
    3) creating many entries: Entry.objects.bulk_create([
        Entry(headline = "this is a test"),
        Entry(headline = "this is only a test"),
    ])
'''
#importing data in database to be used in the html document:
# from .models import Book
def index(request):
    books = Book.objects.all()
    context={
        "books" : books
    }
    return render(request,"book_outlet/index.html",context)
# {% for book in books %}
#     <li> {{book.title}} (rating:{{book.rating}})</li>
# {% endfor %}
#displaying data of a particular row:
def book_detail(request,id):
    book = Book.objects.get(pk=id)
    context = {
        "title" : book.title,
        "author" : book.author,
        "rating" : book.rating,
    }
    return render(request,"book_outlet/index.html", context)
#Raising 404 error if book is not there:
from django.shortcuts import get_object_or_404
def book_detail(request,id):
    book = get_object_or_404(Book,pk=id)
    context = {
        "title" : book.title,
        "author" : book.author,
        "rating" : book.rating,
    }
    return render(request,"book_outlet/index.html", context)
# Good practice to create a function which returns the "valid url" from "url with dynamic element" using the reverse function:
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
    def get_absolute_url(self):
        return reverse("book-detail",args=[self.id])
book = Book.objects.get(pk=id)
# <a href="{{book.get_absolute_url}}">{{book.title}}</a>
