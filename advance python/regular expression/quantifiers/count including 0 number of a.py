import re
x='a*' #count including 0 number of a ,it read the position of all characters
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start(),match.group())