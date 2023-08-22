
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))

if year < 1 or month < 1 or month > 12 or day < 1:
        print("The date is not valid.")


if month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        if day <= 29:
            print("The date is valid.")
    elif day ==29:
         print("The date is not valid.")
         
elif month in [4, 6, 9, 11]:
    if day <= 30:
        print("The date is valid.")
    else:
        print("The date is not valid.")
         
         
         
else:
    print("The date is valid.")
   
 