import re
count=0
matcher=re.finditer('ab','abaabbab')
for match in matcher:
    print("match avaiable at",match.start())#return positions or index number
    print("group:",match.group())         #which object to find "ab"
    count+=1
print("count:",count)