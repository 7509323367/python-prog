import time
'''print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))

d=time.localtime(time.time())
print(str(d.tm_mday)+":"+str(d.tm_mon)+":"+str(d.tm_year))#count time in local time
import time
print(time.asctime(time.localtime(time.time())))#count time in static time
second = time.time()
print("second since epoch",second)

import calendar
print(calendar.month(2022,8)) #show is month cal
print(calendar.firstweekday())
if(calendar.isleap(int(input("enter number")):    #show is leap year
    print("the year is leap year")
else:
    print("the year is not leap year")
print(calendar.leapdays(1950,2022))    #leapyear count
print("the calender of year 2022 is",2022)
print(calendar.calendar(2022))   #show is year calender
from datetime import date            #count is dob
a=date(2021,1,5)
b=date(1996,12,13)
#print(type(a))
months=a.month-b.month
years=a.year-b.day

days=a.day-b.day
print('{0}years,{1}months,{2}days',format(years,months,days))
from datetime import date
a = date(2021,1,5)
b = date(1995,9,25)
#print(type(a))
months=a.month-b.month
years = a.year-b.year
days = a.day-b.day
print(int('{0}years,{0}months,{0}days',format(years.months,days)))

# date of borth count'''
import datetime
cy=datetime.date.today().year
cm=datetime.date.today().month
cd=datetime.date.today().day
by=int(input("enter your birth year"))
bm=int(input("enter your birth month"))
bd=int(input("enter your birth date"))
ay=cy-by
am=abs(cm-bm)
ad=abs(cd-bd)
print(ay,am,ad)
'''import calendar
from datetime import date
year=int(input("enter the your birth year="))
month=int(input("enter the your birth month="))
day=int(input("enter the your birth day="))
current_dy=(date.today().year)
current_mt=(date.today().month)
current_dy=(date.today().day)
age_y=current_yr-year
age_m=current_mt-month
age_d=day-current_dy
if age_d<0 or age_m<0:
    age_y=age_y-1
    print("yor are",age_y,"years",age_m,"months",age_d,"days olds")'''

















