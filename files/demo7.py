#age>50,fname,lname,age,country
f=open("/Users/Aravind/Desktop/data/customer","r")
for line in f:
    data=line.rstrip("\n").split(",")
    fname=data[1]
    lname=data[2]
    age=data[3]
    country=data[-1]
    list=([fname,lname,age,country])
    a=int(list[2])
    if(a>50):
        print(list)