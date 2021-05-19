#word count

#split function
line="hai hello hai hello how what what where how what hello hai hello"
words=line.split(" ") #split function using space
print(words)
dic={}
for i in words:
    if(i not in dic):
        dic[i]=1
    else:
        dic[i]+=1
for i in dic:
    print(i,':',dic[i])
res=dic.values()#to store the values in dictionary
high=max(res)#to find the maximum value in dictionary
for i in dic:
    if(dic[i]==high):
        print("The maximum word is",i,':',dic[i])

