import re
x='a{2}' #no of position
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start(),match.group())