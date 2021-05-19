# f=open("news","r")
# lst=[]
# lst1=[]
# dic={}
# for i in f:
#     lst.append(i.rstrip(".\n"))
# print(lst)
# for i in lst:
#     words=i.split(" ")
# for j in words:
#     lst1.append(j.rstrip("."))
# for i in lst1:
#     if(i not in dic):
#         dic[i]=1
#     else:
#         dic[i]+=1
# print(dic)

f=open("news","r")
dic={}
for lines in f:
    data=lines.rstrip("\n").split(" ")
    for word in data:
        if(word not in dic):
            dic[word]=1
        else:
            dic[word]+=1
print(dic)
for k,v in dic.items():
    print(k,",",v)


