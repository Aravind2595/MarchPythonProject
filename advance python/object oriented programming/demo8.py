class Person:
    def __init__(self,name,age,gender): #__init__ it is usedonly for initialization purpose only
        self.name=name
        self.age=age
        self.gender=gender
    def printval(self):
        print(self.name,self.age,self.gender)
pe=Person("Aravind",26,"Male") #by using initialization constructor value must be pass inside class object
pe.printval()