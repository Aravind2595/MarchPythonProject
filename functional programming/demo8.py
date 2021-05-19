lst1=[10,20]
lst2=[30,40]

#[(10,30),(10,40),(20,30),(20,40)]
pairs=[(num1,num2) for num1 in lst1 for num2 in lst2]
print(pairs)