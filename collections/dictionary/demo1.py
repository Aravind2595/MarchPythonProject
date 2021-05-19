#employee=id,name,desig,salary

#1 employee name
#2 company key check
#3 add company key and value add
#salary+5000
#key value pairs print

employ={'ID':1000,'name':'Aravind','Desig':'Developer','salary':25000}

print(employ['name'])
if("company" not in employ):
    print("company not in employee dictionary")
    employ['company']='luminar'
employ['salary']+=5000
for i in employ:
    print(i,':',employ[i])
