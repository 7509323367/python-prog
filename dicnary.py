x={"rno":1001,"sname":"manish","branch":"cs","fees":1500}
'''x["rno"]=1001
del x["rno"]
x.update({"sem":"3rd"})
x.update({"class":"4th"})
l=[]
for k in x:
    print("key is",k,"and value is",x[k])
    l.append(k)
for i in range(len(l)-1,-1,-1):
    print("key is",l[i],"and value is",x[l[i]])'''
key=[]
val=[]
for 

