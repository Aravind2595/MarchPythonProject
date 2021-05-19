import re
x='^a' #check starting with a consider complete string
r="aaa abc aaaa aa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start(),match.group())