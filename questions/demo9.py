# 5. What is method overriding give an example using Books class?
#the method overriding is a process where if the method name of base class and subclass are same and the arguments in the method also same,
#while executing the program the method of subclass is selected instead of method in base class

class Person:
    def set(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print("name:",self.name)
        print("age:",self.age)
        print("gender:",self.gender)
class Employee(Person):
    def set(self,desig,company,salary):
        self.desig=desig
        self.company=company
        self.salary=salary
        print("desig:",self.desig)
        print("company:",self.company)
        print("salary:",self.salary)
emp=Employee()
emp.set("Anu",20,"Female")