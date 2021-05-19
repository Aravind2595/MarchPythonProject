class Vehicle:
    def type(self,name,tyres,seat):
        self.name=name
        self.tyres=tyres
        self.seat=seat
        print("name:",self.name)
        print("tyres:",self.tyres)
        print("seat:",self.seat)
car=Vehicle()
car.type("tata",4,6)

bike=Vehicle()
bike.type("yamaha",2,2)

auto=Vehicle()
auto.type("bajaj",3,4)


