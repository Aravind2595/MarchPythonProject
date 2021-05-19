#read low to upper
#sum even number
#sum odd number
low=int(input("Enter the lower limit"))
upp=int(input("Enter the upper limit"))
osum=0
esum=0
for i in range(low,(upp+1)):
    if(i%2==0):
        esum+=i
    else:
        osum+=i
print("odd sum is",osum)
print("even sum is",esum)

