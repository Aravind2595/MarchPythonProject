import re
x='[^a-zA-Z0-9]' #to find special symbols
matcher=re.finditer(x,"abt c&5Akz")
for match in matcher:
    print(match.start(),match.group())