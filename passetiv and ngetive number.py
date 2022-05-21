num=int(input("enter the num"))
if num<=9 and num>=0:
    print("one digit positive")
elif num>=-9 and num<=0:
    print("one digit nagative")
elif num<100 and num>=10:
    print("two digit positive")
elif num>-100 and num<=10:
    print("two digit nagative")
else:
    print("no is above")
          
