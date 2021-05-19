num1=int(input("Enter no1"))
num2=int(input("Enter mo2"))

try:
    res=num1/num2
    print(res)
except Exception as e:
    print(e.args)