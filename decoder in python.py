'''def fun1(f):
    print("welcome")
    return f
def fun2(f):
    print("fun2")
    return f
@fun2
@fun1
def fun():
    print("hello world")
fun()
output-:
welcome
fun2
hello world'''
##wap calculet addision fist other the extende the multiplcation also function
'''a,b=10,2
def multi(f):
    print(a*b)
    return f
@multi
def addition():
    print(a+b)
    addition()
output-:
    20'''
###exampal -:2

def smart_divide(func):

    def inner(a,b):

        print("i am going to divaid",a,"and",b)
        if b==0:
            print("woops! can not divide")
            return
        return func(a,b)
    return inner 

@smart_divide
def divide(a,b):
    print(a/b)
divide(10,2)
















