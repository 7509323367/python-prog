'''def addition():
    a=52
    b=85
    c=a+b
    print(c)
def substraction():
    a=52
    b=85
    c=a-b
    print(c)
addition()
substraction()
def si():
    p=5000
    r=5
    t=3
    si=p*r*t/100
    return(si)
res=si()
def addition():
    a=45
    b=87
    print("result is",(a+b))
def substraction():
    x= 89
    y= 45
    print("result is",(x-y))
addition()
res=substraction()
print(res)
def addition(*x):
    for x1 in x:
        print("result is",x1)
addition(100,4,23,34,45,5,67)
sum=lambda x,y:x+y
print(sum(10,20))

def  calcMax(*x):
    m=0
    for d in x:
        if m<d:
           m=d
    else:
        print(m)

calcMax(10,23,49,84,48,5)

def temp():
    f=int(input("enter the number"))
    f=((9*f)+160)*5
    print(f)
temp()
                
def sqr():
     a=int(input("enter the number"))
     sqr=a*a
     print(sqr)
def cube():
     b=int(input("enter the number"))
     cube=b*b*b
     print(cube)
sqr()
cube()'''
a=sqr
b=cube
a=int (input("enter the number"))
sqr=a*a
print(sqr)
b=int(input("enter the number"))
cube=b*b*b
print(cube)









    
