#dictionary

# dic={} #used to define dictionary as empty dictionary

#key-value pairs :used to store elements inside dictionary

#example
#name:Luminar,loc:kakkanad,course:python

#key: name,loc,course
#value:luminar,kakkanad,python
# dic={'name':'luminar','lo':'kakkanad','course':'python','marks':250,'data':10.750} #support hetrogenous data
# print(dic)   #insertion order preserved

dic={'name':'luminar','lo':'kakkanad','age':25,'age':30} #not supported duplicates key
print(dic)
dic1={'name':'luminar','loc':'kakkanad','age':25,'mark':30} #support duplicate value
print(dic1)

#the value is fetched using the corresponding key
print(dic1['name'])
print(dic1["loc"])

#name:luminar
#loc:kakkanad
#age:25
#mark:25
for i in dic1:
    print(i,':',dic1[i])
#dictionary is mutable
dic1['age']=30
dic1['mark']+=20
print(dic1)

#value deletion
del dic1['name']
print(dic1)
dic1.pop('loc')
print(dic1)

#total: 150
print("total" in dic1)
dic1["total"]=150
print(dic1)
