#sorting without using sorted
lst=[2,8,9,5,12,4,1,14,10,3,15,7]
for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        if(lst[i]>lst[j]):
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp
print(lst)





