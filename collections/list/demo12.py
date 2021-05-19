lst=[]
#1 to 100 add
#print prime number

for i in range(1,101):
    lst.append(i)
for k in lst:
    flag=0
    if(k>1):
      for j in range(2,k):
        if(k%j==0):
             flag=1
             break
      if(flag==0):
        print(k,end=" ")

