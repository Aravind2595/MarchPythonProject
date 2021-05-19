#nested if
#read 3elementsandprint second largest number
num1=int(input("Enter the number1"))
num2=int(input("Enter the number2"))
num3=int(input("Enter the number3"))
if(num1>num2)&(num1>num3):
   if(num2>num3):
       print(num2,"second largest")
   else:
       print(num3,"second largest")
elif(num2>num1)&(num2>num3):
    if(num1>num3):
        print(num1,"second largest")
    else:
        print(num3,"second largest")
elif(num3>num1)&(num3>num2):
    if(num1>num2):
        print(num1,"second largest")
    else:
        print(num2,"second largest")
