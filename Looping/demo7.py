#lower limit and upper limit and read even number
low=int(input("Enter the lower limit"))
upp=int(input("Enter the upper limit"))
while(low<=upp):
    if(low%2==0):
        print(low)
    low+=1