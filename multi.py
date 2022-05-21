y=[1,[2,3,[4,5]],[6,[7,8]]]
y1=y[0:1]
print(y1)
y2=y[1:2]
print(y2)
y21=y2[0]
print(y21)
y22=y21[0:2]
print(y22)
y23=y21[2:3]
print(y23)
y24=y23[0]
print(y24)
y3=y[2:]
print(y3)
y31=y3[0]
print(y31)
y32=y31[0:1]
print(y32)
y33=y31[1:2]
y34=y33[0]
print(y34)
y35=y34[0]
print(y35)
print(y1+y22+y24+y32+y34)




