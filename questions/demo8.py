#4.Create an Animal class using constructor and build a child class for Dog?

class Animal:
    def __init__(self,age,gender):
        self.age=age
        self.gender=gender
        print("age:",self.age)
        print("gender:",self.gender)
class Dog(Animal):
    def __init__(self,breed,color,age,gender):
        super().__init__(age,gender)
        self.breed=breed
        self.color=color
        print("Breed:",self.breed)
        print("color:",self.color)
do=Dog("Rottweiler","black",3,"male")
