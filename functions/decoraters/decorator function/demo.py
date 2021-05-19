#decorator function is used to add additional feature to a function without modifying it
#it can be used to reduce the code length avoiding multiple typing
def shuffle_values(func):
    def wrapper(no1,no2):
        if no1<no2:
            no1,no2=no2,no1
        return func(no1,no2)
    return wrapper

@shuffle_values
def div(num1,num2):
    return num1/num2

@shuffle_values
def sub(num1,num2):
    return num1-num2
print(div(2,10))
print(sub(2,10))