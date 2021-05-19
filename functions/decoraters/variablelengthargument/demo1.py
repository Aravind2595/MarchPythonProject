def print_employee(**kwargs): #store in dictionary format in key value format
    for k,v in kwargs.items():
        print(k,":",v)

print_employee(id=100,name="Aravind",salary=5000)