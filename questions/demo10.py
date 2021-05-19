# 6. Create objects of the following file and print the details of student with maximum mark?
# anu,1,bca,200 rahul,2,bba,177 vinod,3,bba,187 ajay,4,bca,198 maya,5, bba,195
class Student:
    def __init__(self,name,rollno,course,mark):
        self.name=name
        self.rollno=rollno
        self.course=course
        self.mark=mark
    def __str__(self):
        return self.name+"\n"+self.rollno+"\n"+self.course+"\n"+str(self.mark)
score=0
f=open("copy","r")
for line in f:
    data=line.rstrip("\n").split(",")
    if(score<int(data[3])):
       name=data[0]
       rollno=data[1]
       course=data[2]
       mark=int(data[3])
       score=int(data[3])
st=Student(name,rollno,course,mark)
print(st)

