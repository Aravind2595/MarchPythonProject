#syntax

#filter(fn,iterable)


lst=[1,2,3,4,5,6,7,8,9,10]
# def even(num):
#     return num%2==0
#
# ev=list(filter(even,lst))
# print(ev)
ev=list(filter(lambda num:num%2==0,lst))
print(ev)