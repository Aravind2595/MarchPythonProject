#temperature find the maximum temperature in each year
f=open("/Users/Aravind/Desktop/data/Temperature")
dic={}
for line in f:
    data=line.rstrip("\n").split(" ")
    print(data)
    if(data[0] not in dic):
        year=data[0]
        dic[year]=data[1]
    else:
        year=data[0]
        temp=int(data[1])
        if(int(dic[year])<temp):
            dic[year]=str(temp)
for i in dic:
    print(i,':',dic[i])


