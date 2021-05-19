#list=[10,20,30,40]==>f(x) [100,400,900,1600]
#syntax

#map(fn,iterable)

lst=[1,2,3,4,5,6,7,8,9]
# def sq(num):
#     return num*num
#
# s=list(map(sq,lst))
# print(s)

s=list(map(lambda num:num*num,lst))
print(s)

squares=list(map(lambda num:num**2,lst))
print(squares)