lst=[2,4,6,7,1,5,8,3,9]
ls=sorted(lst)
print(ls)
n=int(input("Enter the number to search"))
low=0
upp=(len(ls)-1)
flag=0
while(low<=upp):
 mid=(low + upp)//2
 if(n>ls[mid]):
     low=mid+1
 elif(n<ls[mid]):
     upp=mid-1
 elif(n==ls[mid]):
     flag=1
     break
if(flag>0):
    print("Element found")
else:
    print("Element not found")

