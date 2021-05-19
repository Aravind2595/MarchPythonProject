# lst=[]
# for i in range(1,51):
#     lst.append(i)
# print(lst)

# lst=[i for i in range(1,51)]
# print(lst)

# lst=[i for i in range(1,50) if i%2==0]
# print(lst)

lst=[i*i if i%2==0 else i*i*i for i in range(1,50)]
print(lst)

lst=['even' if i%2==0 else 'odd' for i in range(1,50)]
print(lst)