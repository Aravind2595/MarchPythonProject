#create a  list and add elements
#read a element from console
#element found output
#linear search : increase program complexity
list=[1,5,3,7,8,4,9,6,10,2]
print(list)
n=int(input("Enter the number to be search"))
flag=0
for i in list:
    if(n==i):
        flag=1
        break
if(flag==1):
    print("Element found")
else:
    print("Element not found")
#linear search : increase program complexity


