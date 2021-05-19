#multilevel inheritance/ hierarchial inheritance
class Parent:
    def m1(self):
        print("Inside Parent")
class Child(Parent):
    def m2(self):
        print("Inide Child")
class Subchild(Child):
    def m3(self):
        print("Inside Subchild")
obj=Subchild()
obj.m1()
obj.m2()
obj.m3()
obj2=Child()
obj2.m1()
obj2.m2()