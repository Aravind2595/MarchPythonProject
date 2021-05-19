import re
x='[^abc]' #to find except a,b,c
matcher=re.finditer(x,"abt c&5kz")
for match in matcher:
    print(match.start())
    print(match.group())