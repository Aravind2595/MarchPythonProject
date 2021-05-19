class Student:
    school="S.N.D.P H.S.S"
    def setval(self,name,age,std,rollno):
        self.name=name
        self.age=age
        self.std=std
        self.rollno=rollno
    def printval(self):
        print("name:",self.name)
        print("age:",self.age)
        print("standard:",self.std)
        print("rollno:",self.rollno)
        print("school:",Student.school,"\n")
st1=Student()
st1.setval("Aravind",14,8,4)
st1.printval()

st2=Student()
st2.setval("Akhil",9,4,2)
st2.printval()