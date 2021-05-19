class Student:
    def __init__(self,name,rollno,dept,mark):
        self.name=name
        self.rollno=rollno
        self.dept=dept
        self.mark=mark
    def printval(self):
        print("Name:",self.name)
        print("Rollno:",self.rollno)
        print("Department:",self.dept)
        print("Mark:",self.mark)
    def __str__(self):
        return self.name
lst=[]
f=open("wrk","r")
for line in f:
    data=line.rstrip("\n").split(",")
    # if(int(data[3])>190):
    #     st=Student(data[0],data[1],data[2],data[3])
    #     st.printval()
    name=data[0]
    rollno=data[1]
    course=data[2]
    mark=int(data[3])
    st = Student(name,rollno,course,mark)
    lst.append(st)
for i in lst:
    if i.mark>190:
        print(i)