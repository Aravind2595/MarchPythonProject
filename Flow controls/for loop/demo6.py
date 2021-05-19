#check a given number is prime or not
num=int(input("Enter the number"))
flag=0
for i in range(2,num):
    if(num%i==0):
       flag=1
if(flag>0):
    print(num," is not a prime number")
if(flag==0):
    print(num,"is a prime number")


