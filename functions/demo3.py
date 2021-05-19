#create a function to find factorial of number

def fac():
    num1=int(input("Enter the number"))
    res=1
    for i in range(1,num1+1):
        res*=i
    print(res)
fac()

def fac(num1):
    res=1
    for i in range(1,num1+1):
        res*=i
    print(res)
fac(5)

def fac(num1):
    res=1
    for i in range(1,num1+1):
        res*=i
    return res
data=fac(5)
print(data)