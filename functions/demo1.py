#functions
#.............

#syntax
#..........

#def fnname(argument1,argument2):
    #fn statement

#callinf fuction name
#.......................

#fnname() #using fnname

#1.fn without argument and no return type
#2.fn with argument and no return type
#3. fn with argument and return type

#1.fn without argument and no return type

# def add():
#     num1=int(input("Enter number1"))
#     num2=int(input("Enter number2"))
#     sum=num1+num2
#     print(sum)
# add()

# def multi():
#     num1 = int(input("Enter number1"))
#     num2 = int(input("Enter number2"))
#     total=num1*num2
#     print(total)
# multi()

#2.fn with argument and no return type

# def sum(num1,num2):
#     res=num1+num2
#     print(res)
# sum(10,40)
# sum(50,60)

# def div(num1,num2):
#      res=num1/num2
#      print(res)
# div(6,3)


#3. fn with argument and return type

# def sum(no1,no2):
#     res=no1+no2
#     return res
# data=sum(50,40)
# print(data)
#
# data1=sum(10,20)
# print(data1)

#1
#......

def sum():
    num1=int(input("Enter the number1"))
    num2=int(input("Enter the number2"))
    add=num1+num2
    print(add)
sum()

#2
#....

def sum(no1,no2):
    add=no1+no2
    print(add)
sum(2,3)

#3
#......

def sum(no1,no2):
    add=no1+no2
    return add
data=sum(3,5)
print(data)