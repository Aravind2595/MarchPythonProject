#rstrip function used to remove last element like"\n" or ending char
#lstrip is used to remove the first element or starting char
f=open("numbers","r")
lst=[]
for num in f:
    lst.append(int(num.rstrip("\n"))) #int is used to convert the str to integer
print(lst)
print(sum(lst))
