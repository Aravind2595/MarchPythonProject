class Person:
    def set(self,job,desig,company):
        self.job=job
        self.desig=desig
        self.company=company
        print("job:",self.job,"designation:",self.desig,"company:",self.company)
class Employee(Person):
    def set(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        print("name:",self.name,"age:",self.age,"salary:",self.salary)
emp=Employee()
emp.set("Engineer","Developer","Luminar")
