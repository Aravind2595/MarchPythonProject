st={1,2,3,4,5}

#add function
st.add(6)
st.add("luminar")
st.update([50,60]) #update function to add multiple elements
print(st)
st.remove(60)   #value should be in the set unless it show key error
print(st)
st1={1,2,3,4,5,6,7,8,9,10}
st1.discard(11) #if the element is not present in the list it will not show error
print(st1)
st1.pop() #remove first element
print(st1)