n=input("Enter a string")
list=[]
for i in n:
    list.append(i)
flag=0
for j in range(0,(len(list)//2)):
     if(list[j]==list[-j-1]):
        flag=1
if(flag==1):
    print(n,"is a palindrome")
else:
    print(n,"is not a palindrome")

