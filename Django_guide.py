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
#Template Inheritance:

