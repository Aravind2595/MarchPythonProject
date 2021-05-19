#combination of upper case and lower case number ending with a number
import re
n=input("Enter the input")
x='[a-zA-Z]+\d{1}$'
match=re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("invalid")