n=0
top=0
size=int(input("Enter the size"))
lst=[]
def insert():
    global top,size
    if top>=size:
        print("queue is full")
    else:
        p=int(input("Enter the element want to insert"))
        lst.append(p)
        top+=1
        for i in lst:
            print(i)
def delete():
    global top, size
    if top <= 0:
        print("queue is empty")
    else:
        lst.pop(0)
        top -= 1
        for i in lst:
            print(i)
while(n!=1):
    print("Enter the operation want to perform")
    num = int(input("1 (insert)\n2 (delete)"))
    if(num==1):
       insert()
    elif(num==2):
        delete()