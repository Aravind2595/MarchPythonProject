import re
n=input("Enter the number")
x='[+][9][1]\d{10}$'
match=re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("invalid")
