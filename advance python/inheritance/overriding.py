#same method name same parameters in this time the child class will override parent class method
class Parent:
    def properties(self):
        print("10 lakh rs,2 car")
    def marry(self):
        print("With ram")
class Child(Parent):
    def marry(self):
        print("with arun")
c=Child()
c.marry()