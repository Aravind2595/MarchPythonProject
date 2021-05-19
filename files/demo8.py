#profession doc, fname,lname,profession,age,country
f=open("/Users/Aravind/Desktop/data/customer","r")
for line in f:
    data=line.rstrip("\n").split(",")
    pro=data[4]
    fname=data[1]
    lname=data[2]
    age=data[3]
    country=data[-1]
    list=([fname,lname,pro,age,country])
    if(list[2]=="Doctor"):
        print(list)