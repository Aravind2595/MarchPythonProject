#read a numberand print a reverse
#1234
# num=int(input("Enter the number"))
# while(num!=0):
#      ans=num%10
#      num=num//10
#      print(ans,end=' ')

num=int(input("Enter the number"))
res=0
while(num!=0):
    digit=num%10
    res=(res*10)+digit
    num=num//10
print(res)