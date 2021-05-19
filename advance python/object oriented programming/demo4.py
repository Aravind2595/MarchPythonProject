x=int(input("Enter the number1"))
y=int(input("Enter the number2"))
class Addition:
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def op(self):
        print(self.num1+self.num2)
add=Addition()
add.sum(x,y)
add.op()