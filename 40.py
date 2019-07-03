s1=int(input())
d1,d2=0,1
print(d2,end=" ")
for i in range(1,s1):
 d3=d1+d2
 print(d3,end=" ")
 d1,d2=d2,d1
