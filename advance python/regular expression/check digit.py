import re
x='\d' #to check digit
matcher=re.finditer(x,"abt c&5Akz")
for match in matcher:
    print(match.start(),match.group())