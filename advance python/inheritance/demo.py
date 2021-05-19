#person child parent student
#child and parent inherit person
#student inherit child class
class Person:
    def set(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print("name:",self.name)
        print("age:",self.age)
        print("gender:",self.gender)
class Parent(Person):
    def set1(self,salary,job):
        self.salary=salary
        self.job=job
        print("salary:",self.salary)
        print("job:",self.job)
class Child(Person):
    def set2(self,school):
        self.school=school
        print("school:",self.school)
class Student(Child):
    def set3(self,rollno,std):
        self.rollno=rollno
        self.std=std
        print("Roll no:",self.rollno)
        print("standard:",self.std)
obj1=Student()
obj1.set("Aravind",10,"Male")
obj1.set2("S.N.D.P H.S.S")
obj1.set3(4,5)
obj2=Parent()
obj2.set("Thulasi",40,"Female")
obj2.set1("NIL","HOME MAKER")

