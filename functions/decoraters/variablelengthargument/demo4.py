employees={
    1000:{"eid":1000,"name":"ajay","salary":25000,"designation":"Developer"},
    1001:{"eid":1001,"name":"vijay","salary":22000,"designation":"Developer"},
    1002:{"eid":1002,"name":"arun","salary":26000,"designation":"qa"},
    1003:{"eid":1003,"name":"varun","salary":27000,"designation":"ba"},
    1004:{"eid":1004,"name":"ram","salary":20000,"designation":"mrkt"}
}
def print_employee(**kwargs):
    id=kwargs["id"]
    prop=kwargs["prop"]
    if id in employees:
        print(employees[id]["name"])#employees[1000]
        print(employees[id][prop]) #employees salary
    else:
        print("invalid id")
print_employee(id=1000,prop="salary")