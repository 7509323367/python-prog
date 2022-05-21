'''fruits=["apple","banana","chary","kivi","mango"]
newlist=[x for x in fruits if 'a' in x]
print(newlist)


prime num
squar and qube
x=[10,30,40,23,49,45]
   y=[a for a in x if a%2==0]
print(y)
y=[a*a if a%2==0 else a*a*a for a in x]
print(y)
x=[-1,-4,5,-6,2,9,1]
y=[a for a in x if a>0]
print(y)
x=[1995,1698,2005,2008,2004]
y=[a for a in y if x%100==0 or x%4==0 or x%400!=0]
print(y)'''

x=[10,30,40,23,49,45]
y=[a for a in x if a%5==0 or a%3==0]
print(y)
