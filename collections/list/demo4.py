lst=[500,10,20,30,1000,40,50,60,70,100,80,90]
print(sum(lst))
res=0
for i in lst:
    if(res<i):
        res=i

print(res)

#max to find maximum value
print(max(lst))

#min to find minimum value
print(min(lst))