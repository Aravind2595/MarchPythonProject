import re
x='\W' #to check special characters
matcher=re.finditer(x,"abt c&5Akz")
for match in matcher:
    print(match.start(),match.group())