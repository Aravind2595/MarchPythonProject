#Create a child class Bus that will inherit all of the variables and methods of Vehicle class?

class Vehicle:
    def setval(self,tyre,type,gear,seat):
        self.tyre=tyre
        self.type=type
        self.gear=gear
        self.seat=seat
    def printval(self):
        print("tyre:",self.tyre)
        print("Disel or petrol:",self.type)
        print("gear:",self.gear)
        print("seat:",self.seat)
class Bus(Vehicle):
    def set(self,company,ac):
        self.company=company
        self.ac=ac
    def print(self):
        print("company:",self.company)
        print("A/C or Non A/C:",self.ac)
obj=Bus()
obj.set("Ashok Leyland","A/C")
obj.setval(6,"Diesel",6,32)
obj.print()
obj.printval()

