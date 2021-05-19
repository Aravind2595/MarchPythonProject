#set

#set cannot define as empty function using curly bracket it will read as dictionary
#set function
st=set()
print(type(st))
st={2,5,7,8,10}
print(st)

st1={2,'sabir',18.5,True,False} #it support hetrogenous data
print(st1)                      #insertion order not preserved

st2={1,1,2,2,5,5,3,3,'luminar','luminar'} #not support duplicates
print(st2)

st3={True,False,0,1}
print(st3)

#its is mutable
st3.add(3)
print(st3)