lst1=[7,8,9,4,3,2,1]
#if num>5 num+1
#else num-1
lst=[]
for i in lst1:
        lst.append(i+1) if i>5 else lst.append(i-1) #ternary operation
print(lst)
ls=list(map(lambda num:num+1 if num>5 else num-1,lst1))
print(ls)

