import re
x='[a-z]' #to find small letters from a to z
matcher=re.finditer(x,"abt c&5kz")
for match in matcher:
    print(match.start(),match.group())