def test(func):
    def wrapper(**kwargs):
        age = kwargs["age"]
        health = kwargs["health_issue"]
        if age>65 or health==True:
             return func(**kwargs)
        else:
             raise Exception("Criteria not met")
    return wrapper
@test
def vaccination_portal(**kwargs):
    print("request allowed location ekm")
try:
    vaccination_portal(name="ram",age=25,address="address",health_issue=False)
except Exception as e:
    print(e.args)