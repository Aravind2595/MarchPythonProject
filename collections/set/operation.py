#union combine two set by eliminating duplicate element
st1={1,2,3,4,5,6,7,8,9,10}
st2={5,6,7,8,9,10,11,12,13,14,15}

st3=st1.union(st2)
print(st3)

#intersection collecting common element from two set

st4=st1.intersection(st2)
print(st4)

#difference :collecting elements from set1 excluding common elements in set2
st5=st1.difference(st2)
print(st5)