import re
x='[0-9]' #to find digits
matcher=re.finditer(x,"abt c&5Akz")
for match in matcher:
    print(match.start(),match.group())