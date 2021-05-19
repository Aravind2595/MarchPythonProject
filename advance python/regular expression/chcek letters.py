import re
x='\w' #to check words and number except special character
matcher=re.finditer(x,"abt c&5Akz")
for match in matcher:
    print(match.start(),match.group())