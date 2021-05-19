employees=[
    {"eid":1000,"name":"ajay","salary":25000,"designation":"Developer"},
    {"eid":1001,"name":"vijay","salary":22000,"designation":"Developer"},
    {"eid":1002,"name":"arun","salary":26000,"designation":"qa"},
    {"eid":1003,"name":"varun","salary":27000,"designation":"ba"},
    {"eid":1004,"name":"ram","salary":20000,"designation":"mrkt"}
]
enames=[emp["name"] for emp in employees]
print(enames)

developers=[emp for emp in employees if emp["designation"]=="Developer"]
print(developers)
#highest salary
salary=max([emp["salary"] for emp in employees])
print(salary)