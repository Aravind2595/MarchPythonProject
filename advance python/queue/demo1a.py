n=0
front=0
rear=0
size=int(input("Enter the size"))
lst=[]
def insert():
    global front,rear,size,lst
    if rear>=size:
        print(".....queue is full.....")
    else:
        p=int(input("......Enter the element want to insert......"))
        lst.insert(rear,p)
        rear+=1
        for i in range(front,rear):
            print(lst[i])
def delete():
    global front,rear,size,lst
    if front== rear:
        print(".....queue is empty.....")
    else:
        front+=1
        for i in range(front,rear):
            print(lst[i])
while(n!=1):
    print(".....Enter the operation want to perform.....")
    num = int(input("1 ::insert\n2 ::delete"))
    if(num==1):
       insert()
    elif(num==2):
        delete()