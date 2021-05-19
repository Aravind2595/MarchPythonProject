#2. Create an example for three types of inheritance in one program by using Person as main class?

class Person:
    def set(self,age,gender):
        self.age=age
        self.gender=gender
        print("age:",self.age)
        print("gender:",self.gender)
class Father(Person):
    def set1(self,name,company,job,relation):
        self.name=name
        self.company=company
        self.job=job
        self.relation=relation
        print("name:",self.name)
        print("company:",self.company)
        print("job:", self.job)
        print("relation:",self.relation)
class Mother(Person):
    def set2(self,name1,company1,job1,relation1):
        self.name1=name1
        self.company1=company1
        self.job1=job1
        self.relation1=relation1
        print("name:", self.name1)
        print("company:", self.company1)
        print("job:", self.job1)
        print("relation:", self.relation1)
class Child(Father,Mother):
    def set3(self,name2,school,std,mark):
        self.name2=name2
        self.school=school
        self.std=std
        self.mark=mark
        print("name:",self.name2)
        print("school:",self.school)
        print("standard:",self.std)
        print("mark:",self.mark)
ch=Child()
ch.set3("Aravind","S.N.D.PH.S.S",10,550)
ch.set1("Venu","Cochin Shipyard","Charge man","Father")
ch.set2("Thulasi","nil","Home maker","Mother") # multiple inheritance father & mother --> Child (considering above sentance)
ch.set(15,"Male") #multilevel inheritance Person-->Father-->Child
fa=Father()
fa.set1("Anand","Dry Dock","Safety officer","Father")
fa.set(29,"Male") #single inheritance Person-->Father
