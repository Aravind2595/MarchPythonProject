list=[1,2,3,4,5,6]
print(list)
n=int(input("Enter the number"))
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if(n==list[i]+list[j]):
            print(list[i],list[j])