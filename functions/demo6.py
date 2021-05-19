a="hello world"
b=input("Enter the word")
flag=0
for i in a:
    if(b==i):
      flag=1
if(flag==1):
    print("present")
else:
    print("not present")

for i in a:
    if(b==i):
        print("present")
        break



