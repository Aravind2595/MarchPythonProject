#8. When is the finally block executed.Explain with example?
# finally block will execute in all cases even if there is a error or not
a=[1,2,3]
print(a)
num=int(input("Enter the index number"))
try:
    print(a[num])
except:
    print("index should be up to",len(a),"from 0")
finally:
    print("inside finally")