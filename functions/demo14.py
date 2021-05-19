#import pacakage_name.module_name

#variable_name=pacakage_name.module_name.function_name(argument)

#multi calling
#.......................

# import functions.read
# addition=functions.read.add(10, 20)
# print(addition)
# subtraction=functions.read.sub(40, 20)
# print(subtraction)
# multiplication=functions.read.multi(10, 10)
# print(multiplication)
# division=functions.read.div(40, 10)
# print(division)

#single calling
#..................

from functions.demo13 import *  # '*' is used to call all function in the module

addi=add(10,20)
print(addi)
subi=sub(40,20)
print(subi)
mult=multi(2,3)
print(mult)
divi=div(8,4)
print(divi)