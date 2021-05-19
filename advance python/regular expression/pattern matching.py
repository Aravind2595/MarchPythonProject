#pattern matching

#re --package for pattern matching(regular expression)

import re
count=0
matcher=re.finditer('ab','abaabbab') #to find the object in a given string
for match in matcher:
    count+=1
print("count:",count)
