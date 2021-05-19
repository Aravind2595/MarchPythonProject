#nested list
lst=[[1001,'arun',25,1000],[1002,'arjun',26,2000],[1003,'vinu',27,3000],[1004,'binu',28,4000]]
print(lst)
#1001,'arun,25,1000
#1002,'arjun,25,2000
#1003,vinu,27,3000
#1004,binu,28,4000
for i in lst:
    print(i)
#arun
#arjun
#vinu
#binu
for i in lst:
    print(i[1])
#salary above 2000
#names
salary=2000
for i in lst:
    if(i[3]>salary):
        print(i[1])