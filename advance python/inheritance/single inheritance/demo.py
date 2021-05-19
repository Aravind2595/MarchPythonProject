#single inheritance
class Person:  #parent class or base class or super class
    def details(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printdet(self):
        print(self.name)
        print(self.age)
        print(self.gender)
class Student(Person): #child class or sub class or derived class
    def det(self,rollno,school):
        self.rollno=rollno
        self.school=school
    def prints(self):
        print(self.rollno)
        print(self.school)
per=Person()
per.details("Aravind",26,"Male")
per.printdet()
st=Student()
st.det(8,"ABC")
st.prints()
st.details("Anu",20,"female")
st.printdet()