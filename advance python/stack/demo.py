n=0
top=0
size=int(input("Enter the size"))
lst=[]
def push():
    global top,size
    if top>=size:
        print("stack is full")
    else:
        p=int(input("Enter the element want to push"))
        lst.append(p)
        top+=1
        print(lst)
def pop():
    global top, size
    if top <= 0:
        print("stack is empty")
    else:
        lst.pop()
        top -= 1
        print(lst)
while(n!=1):
    print("Enter the operation want to perform")
    num = int(input("1 (push),2 (pop)"))
    if(num==1):
       push()
    elif(num==2):
        pop()


