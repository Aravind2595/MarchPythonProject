import re
x='\D' #to check except digit
matcher=re.finditer(x,"abt c&5Akz")
for match in matcher:
    print(match.start(),match.group())