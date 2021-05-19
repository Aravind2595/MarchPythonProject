a=[1,2,3]
print(a)
num=int(input("Enter the index number"))
try:
    print(a[num])
except:
    print("index should be up to",len(a),"from 0")
