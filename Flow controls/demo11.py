#urban area
age=int(input("Enter the age"))
sex=input("Enter the sex")
if(sex=='f'):
    print("The work is alloted in urban areas")
elif(20<=age<=40):
    print("The work is alloted anywhere")
elif(40<=age<=60):
    print("The work is alloted in urban areas")
else:
    print("error")