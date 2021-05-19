class Employee:
    def setval(self,name,id,depart,salary):
        self.name=name
        self.id=id
        self.depart=depart
        self.salary=salary
        print(self.name,self.id,self.depart,self.salary)
    def __str__(self): #to string method for printing the object
        return self.name+str(self.id)
emp=Employee()
emp.setval("Aravind",1001,"Developer",25000)
print(emp)
