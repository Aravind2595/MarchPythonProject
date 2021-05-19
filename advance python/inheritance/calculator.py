class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        print("Result:",self.num1+self.num2)
    def sub(self):
        print("Result:",self.num1 - self.num2)
    def mul(self):
        print("Result:",self.num1 * self.num2)
    def div(self):
        print("Result:",self.num1 / self.num2)
x=int(input("Enter the number1"))
y=int(input("Enter the number2"))
print("......Enter your choise.......")
n=int(input("1.Addition\n2.Subtaction\n3.Multiplication\n4.Division\n"))
obj=Calculator(x,y)
if(n==1):
   obj.add()
elif(n==2):
    obj.sub()
elif(n==3):
    obj.mul()
elif(n==4):
    obj.div()
else:
    print("Check the option you choose")






