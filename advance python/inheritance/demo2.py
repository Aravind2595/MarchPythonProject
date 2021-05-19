class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("name:",self.name)
        print("age:",self.age)
f=open("student","r")
for line in f:
    data=line.rstrip("\n").split(",")
    st=Student(data[0],data[1])
    st.printval()
