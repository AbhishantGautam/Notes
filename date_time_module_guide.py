import datetime as dt

now = dt.datetime.now() #------> gives today's date and time
year = now.year #--------------> gives current year
month = now.month #------------> gives current month
day_of_week = now.weekday() #--> gives current day

#storing a time object in a variable:
date_of_birth = dt.datetime(year=1998, month=10, day=10)

today = dt.now()
print(today.strftime("%Y%m%d")) #-------> changes the data format to yearmonthdate format
#we can alter date format to our requirements by refering to strftime() function from its documentation