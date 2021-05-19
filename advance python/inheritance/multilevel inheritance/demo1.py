class Person:
    def set(self,name,age):
        self.name=name
        self.age=age
        print("Name:",self.name)
        print("Age:",self.age)
class Employee(Person):
    def set1(self,salary,company):
        self.salary=salary
        self.company=company
        print("Salary:",self.salary)
        print("Company:",self.company)
class Profession(Employee):
    def set2(self,prof):
        self.prof=prof
        print("Profession:",self.prof)
obj=Profession()
obj.set("Aravind",26)
obj.set1(25000,"Luminar")
obj.set2("Developer")