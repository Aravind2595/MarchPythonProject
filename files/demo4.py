f=open("/Users/Aravind/Desktop/data/customer","r")
for line in f:
    data=line.rstrip("\n").split(",")
    fname=data[1]
    age = data[3]
    country = data[-1]
    lst=([fname,age,country])
    if(lst[-1]=="india"):
             print(lst)
#age>50,fname,lname,age,country
#profession doc, fname,lname,profession,age,country