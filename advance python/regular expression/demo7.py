#KL01AJ0000
import re
n=input("Enter the reg no")
x='^[K][L]\d{2}[A-Z]{1,2}\d{4}$'
match=re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("Invalid")
