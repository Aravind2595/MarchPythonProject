#1.copy1 a python program to remove duplicate element from a list
#2.copy1 a python program to find second largest element from a list
#3.copy1 a program to produce a star triangle.
#4.fibnocii series
#5.copy1 a python program to check given sequence is palindrome or not
#code o/p  mail(zip)
#sabirsadaru@gmail.com

lst=[1,2,3,5,4,7,3,7,8,2,5]
list=sorted(lst)
for i in range(0,len(list)):
    for j in range(i+1,len(list)-1):
        if(list[i]==list[j]):
            list.pop(j)
print(list)
