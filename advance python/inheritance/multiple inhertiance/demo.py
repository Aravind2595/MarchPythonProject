#multiple inheritance : in sub class it has more than one base class
class Parent:
    def m1(self):
        print("Inside Parent")
class Child:
    def m2(self):
        print("Inside child")
class Subchild(Child,Parent): #calling base classes
    def m3(self):
        print("Inside subchild")
obj=Subchild()
obj.m1()
obj.m2()
obj.m3()