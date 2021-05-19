#Attendence
totalclass=int(input("enter the total classes held"))
totalattend=int(input("Enter the total attendence"))
attendper=((totalattend/totalclass)*100)
print("the percentage of total attendence is",attendper,"%")
if(attendper<75):
  print("Student is not allowed")
else:
  print("student is allowed")