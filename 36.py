har=input()
ds=0
for i in range(len(har)):
 if(har[i].isdigit() or har[i].isalpha() or har(i)=(" ")):
  continue
 else:
  ds+=1
print(ds)  
