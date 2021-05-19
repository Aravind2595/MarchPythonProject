#count each profession
f=open("/Users/Aravind/Desktop/data/customer","r")
dic={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    data1=data[4]
    if(data1 not in dic):
        dic[data1]=1
    else:
        dic[data1]+=1
print(dic)

