def admin_required(func):
    def wrapper(user,pin):
        if user!="Admin":
            raise Exception("you are not allowed")
        else:
            return func(user,pin)
    return wrapper
@admin_required
def change_pin(user,pin):
    mypin=pin
    return mypin
print(change_pin("user",1000))
print(change_pin("Admin",1001))
