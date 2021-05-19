for i in range(1,6):
    for k in range(1,6-i):
        print(" ",end=" ")
    for j in range(1,(2*i)):
        print("*",end=" ")
    print()
for i in range(1,9):
    for k in range(0,i):
        print(" ",end=" ")
    for j in range(0,9-(2*i)):
        print("*", end=" ")
    print()