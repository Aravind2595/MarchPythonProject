lst=[10,20,21,22,25,26,27,28]
# cnt=1
# res=0

# for i in lst:
#      res=i**cnt
#      cnt+=1
#      print(res)

cnt=len(lst)
j=1
for i in range(0,cnt):
    res=lst[i]**j
    j+=1
    print(res)




