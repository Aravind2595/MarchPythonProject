# 7. Create a valid phone numbers file from the following file?
# +915678905432 +914567890321 765432167 123450987765 +919976532456
f=open("read","r")
import re
f1=open("copy1", "w")
for line in f:
    data=line.rstrip("\n").split(" ")
for i in data:
    x='[+][9][1]\d{10}'
    match=re.fullmatch(x,i)
    if match is not None:
        f1.write(i)
        f1.write("\n")
