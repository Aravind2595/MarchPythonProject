# 9. Write a Python program to find the sequences of one upper case letter followed by lower case letters?
import re
n=input("Enter")
x='^[A-Z][a-z]+'
match=re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("invalid")