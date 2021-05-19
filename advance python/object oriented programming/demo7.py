class Bank:
    bname="ABC Bank"
    def creation(self,name,age,job,account,balance):
        self.name=name
        self.age=age
        self.job=job
        self.account=account
        self.balance=balance
    def deposit(self,money):
        self.money=money
        self.balance=self.money+self.balance
        print("name:",self.name)
        print("age:",self.age)
        print("job:",self.job)
        print("account no:",self.account)
        print("balance:",self.balance)
    def withdraw(self,debit):
        self.debit=debit
        if(self.debit<self.balance):
           self.balance=self.balance-self.debit
           print("name:", self.name)
           print("age:", self.age)
           print("job:", self.job)
           print("account no:", self.account)
           print("balance:", self.balance)
        else:
            print(".......::balance is less::........")
i=0
ac1=Bank()
a=input("Enter your name")
b=int(input("Enter your age"))
c=input("Enter you job")
d=int(input("Enter your account no"))
e=int(input("Enter you balance"))
ac1.creation(a,b,c,d,e)
while (i != 1):
      print("Enter the option\n1.Deposit\n2.withdrawal")
      j = int(input("Enter your choice"))
      if(j==1):
          f=int(input("Enter the amount to deposit"))
          ac1.deposit(f)
      if(j==2):
          g=int(input("Enter the amount to withdraw "))
          ac1.withdraw(g)



