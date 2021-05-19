#same method name and different parameter
class Person:  #parent class or base class or super class
    def det(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print(self.name)
        print(self.age)
        print(self.gender)
class Student(Person): #child class or sub class or derived class
    def det(self,rollno,school):
        self.rollno=rollno
        self.school=school
        print(self.rollno)
        print(self.schoo)
st=Student()
st.det(9,"abc school") #overloading doesn't support in python now normally if the method for parent and base
                        #class is same the method called based on the arguments