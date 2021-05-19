#class:design pattern
#object:real world entity
#references: name that refers a memory location of a object

# class Person: #design pattern
#     def print(self): #function inside a class is called method; self:instance variable
#         print("inside print method")
# pe=Person() #object reference or defining variable as object in class
# pe.print() #calling function inside class

class Person: #design pattern
    def print(self,name,age,gender):#function inside a class is called method; self:instance variable
        self.name=name
        self.age=age
        self.gender=gender
        print("inside print method",self.name,self.age,self.gender)
pe=Person() #object reference or defining variable as object in class
pe.print("Aravind",26,"Male") #calling function inside class

re=Person()
re.print("Amal",24,"Male")