class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("name:",self.name)
        print("age:",self.age)
class Student(Person):
    def __init__(self,rollno,mark,name,age): #arguments in methods in base class must pass in subclass method
        super().__init__(name,age)  #calling arguments from base or super class
        self.rollno=rollno
        self.mark=mark
    def print(self):
        print("rollno:",self.rollno)
        print("Mark:",self.mark)

cr=Student(2,34,"Aravind",26)
cr.printval()
cr.print()



