a=2
def printa():
    global a #global term is ued to call the value of variable outside the function if the variable name is same
    print(a) #unless it is local with different value
printa()
print(a)