#create a function to return a cube of number

def cube(no):
    res=1
    for i in range(0,3):
         res*=no
    return res
data=cube(3)
print(data)
data1=cube(5)
print(data1)


