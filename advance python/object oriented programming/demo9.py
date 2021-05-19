class Employee:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
    def printval(self):
        print(self.name,self.id,self.salary)
obj=Employee("Aravind",1001,25000)
obj.printval()