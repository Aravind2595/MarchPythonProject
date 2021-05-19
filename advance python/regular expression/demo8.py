#mailvalidation
import re
n=input("Enter the mail id")
x='[a-zA-Z0-9_.+-]+[@][a-zA-Z0-9]+\.[a-zA-Z0-9]+$' # character can be defined inside[.] or \. or simply put '.'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")

