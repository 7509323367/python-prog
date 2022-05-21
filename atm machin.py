bal=200
for i in range(1,4):
    pin = input("enter pin code")
    if pin=="1234":
        flag=True
        break
    else:
     print("your pin in incorrect")
     break

while flag:
    i= input("press c for continue,\n press k for credit,\n press d for debit,\n press b for balance inquire,\n press e for exit,")
    if i =="c":
        print("continue")
    elif i =="k":
        amt=int(input("enter amount"))
        bal+=amt
    elif i =="d":
        amt=int(input("enter amount"))
        bal-=amt
    elif i =="b":
        print("your current balance is ",bal)
    
    elif bal<=500:
        print("avilabal balance bal in sapeseant")
    
    else:
        break 


              
