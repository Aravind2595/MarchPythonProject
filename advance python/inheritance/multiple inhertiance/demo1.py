class Father:
    def fa(self):
        print("Inside Father")
class Mother:
    def mo(self):
        print("Inside Mother")
class Child(Father,Mother):
    def chi(self):
        print("Inside Child")
ch=Child()
ch.fa()
ch.mo()
ch.chi()