#maximum amoung three numbers using "&" operation
num1=int(input("Enter the number1"))
num2=int(input("Enter the number2"))
num3=int(input("Enter the number3"))
if(num1>num2)&(num1>num3):
    print(num1,"highest")
elif(num2>num1)&(num2>num3):
    print(num2,"highest")
else:
    print(num3,"highest")
