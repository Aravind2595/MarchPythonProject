def add(*args): #muttiple argument passing ;it will also accept 0 argument
    res=0       #* is important not 'args' eg: *hai or *arg=
    for num in args:#argument will be stored in tuple format
        res+=num
    return res
print(add(10,20,30,40))