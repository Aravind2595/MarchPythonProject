#to create customised exception error raise keyword is using

age=int(input("Enter your age"))
if age>18:
    print("eligible for vaccination")
else:
    raise Exception("not eligible for vaccination")