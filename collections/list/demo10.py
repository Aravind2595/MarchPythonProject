#1 to 100
#add even number to new list
#add odd number to list
lst=[]
even=[]
odd=[]
for i in range(1,101):
     lst.append(i)
print(lst)
for j in lst:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print(even)
print(odd)