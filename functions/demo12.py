print("Select operation")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.divison")
choice=int(input("Enter your choice"))
num1=float(input("Enter the number1"))
num2=float(input("Enter the number"))
def add(x,y):
        return x+y
def sub(x,y):
        return x-y
def multi(x,y):
       return x*y
def div(x,y):
        return x/y

if choice==1:
    print(add(num1,num2))
elif choice==2:
    print(sub(num1,num2))
elif choice==3:
    print(multi(num1,num2))
elif choice==4:
    print(div(num1,num2))
else:
    print("Please check the option")


