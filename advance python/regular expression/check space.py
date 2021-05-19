import re
x='\s' #to check space
matcher=re.finditer(x,"abt c&5Akz")
for match in matcher:
    print(match.start(),match.group())