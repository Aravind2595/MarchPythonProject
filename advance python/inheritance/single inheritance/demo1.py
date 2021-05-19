#person #employee
class Person:
    def setval(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printval(self):
        print(self.name)
        print(self.age)
        print(self.gender)
class Employee(Person):
    def set(self,desig,company):
        self.desig=desig
        self.company=company
    def print(self):
        print(self.desig)
        print(self.company)
per=Person()
per.setval("Aravind",26,"Male")
per.printval()
emp=Employee()
emp.set("Developer","Luminar")
emp.print()
emp.setval("Anu",20,"Female")
emp.printval()