class Student:
    def setval(self,name,std,gender):
        self.name=name
        self.std=std
        self.gender=gender
    def printval(self):
        print("name:",self.name)
        print("standard:",self.std)
        print("gender:",self.gender)
school=Student()
school.setval("Aravind",12,"Male")
school.printval()

college=Student()
college.setval("Aravind","Btech","Male")
college.printval()


