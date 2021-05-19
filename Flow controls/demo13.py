#current year
#current month
#current date

#year
#month
#date

current_year=int(input("Enter the current year"))
current_month=int(input("Enter the current month"))
current_day=int(input("Enter the current day"))
birth_year=int(input("Enter the birth year"))
birth_month=int(input("Enter the birth month"))
birth_day=int(input("Enter the birth day"))
if(current_year<=birth_year)&(current_month<=birth_month)&(current_day<=birth_day):
    print("Please check the values")
elif(current_month>=birth_month)&(current_day>=birth_day):
    year=current_year-birth_year
    month=current_month-birth_month
    day=current_day-birth_day
    print("the age is",year,"years",month,"months and",day,"days old")
elif(current_month<birth_month)&(current_day>=birth_day):
    year = (current_year-1) - birth_year
    month = (current_month+12) - birth_month
    day = current_day - birth_day
    print("the age is", year, "years", month, "months and", day, "days old")
elif(current_month<=birth_month)&(current_day<birth_day):
      year = (current_year-1) - birth_year
      month = ((current_month-1)+12) - birth_month
      day = (current_day+30) - birth_day
      print("the age is", year, "years", month, "months and", day, "days old")


