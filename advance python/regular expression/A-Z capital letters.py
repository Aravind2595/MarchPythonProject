import re
x='[A-Z]' #to find capital letters from a to z
matcher=re.finditer(x,"abt c&Akz")
for match in matcher:
    print(match.start(),match.group())