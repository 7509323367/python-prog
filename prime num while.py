num=int(input("enter the number"))
p=0
i=1
while(i<=num):
    if num%i==0:
        c=p+1
        i=i+1
        if c==2:
            print("prime no")
        else:
            print("not prime")
                             
