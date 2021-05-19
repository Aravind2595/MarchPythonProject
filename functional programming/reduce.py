#can't use reduce directly
#functools
import functools
lst=[7,8,9,4,3,2]

#in reduce two arguments should be passed with lambda
#in map and filter one arguments passed with lambda
total=functools.reduce(lambda no1,no2:no1+no2,lst)
print(total)

highest=functools.reduce(lambda no1,no2:no1 if no1>no2 else no2,lst)
print(highest)