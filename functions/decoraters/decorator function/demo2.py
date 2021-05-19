def vaccination_portal(**kwargs):
    age=kwargs["age"]
    health=kwargs["health_issue"]
    if age>65 or health==True:
         print("request allowed location ekm")
    else:
        print("criteria not met")

vaccination_portal(name="ram",age=25,address="address",health_issue=True)