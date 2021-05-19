#2 type of variable
# static variablr: related to class and "class name"
# instance varibale related to method(function) "self"
#employee name,id,desig,salary,company name
#set value and print value
class Employee:
    company="Luminar" #static variable
    def setval(self,name,id,desig,salary):
        self.name=name
        self.id=id
        self.desig=desig
        self.salary=salary #instance variable
    def printval(self):
        print("name:",self.name)
        print("ID:",self.id)
        print("Designation:",self.desig)
        print("Salary:",self.salary)
        print("Company Name:",Employee.company) #calling static variable
emp=Employee()
emp.setval("Aravind","1001","Professor","25000")
emp.printval()
print("\n")

emp1=Employee()
emp1.setval("Venu","1002","supervisor","50000")
emp1.printval()
