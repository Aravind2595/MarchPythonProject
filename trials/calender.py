year=int(input("Enter the year"))
def is_leap(y):
      if(y%4==0):
          if(y%100==0):
             if(y%400==0):
                 return True
             else:
                 return False
          else:
             return True
      else:
          return False
print(is_leap(year))


