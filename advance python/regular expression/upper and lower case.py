import re
x='[a-zA-Z]' #to find upper case and lower case letter
matcher=re.finditer(x,"abt c&Akz")
for match in matcher:
    print(match.start(),match.group())