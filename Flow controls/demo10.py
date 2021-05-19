#bonus
salary=int(input("Enter the salary"))
service=int(input("Enter years of service"))
if(service>5):
     bonus=((salary*5) / 100)
     print("The bonus amount is",bonus)
else:
    print("The user is not qualified for bonus amount")