import re
x='a{1,3}' #no of position from minimum to maximum
r="aaa abc aaaa aa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start(),match.group())