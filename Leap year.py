#To print leap year with given conditions as such:
#n the Gregorian calendar, three conditions are used to identify leap years:
#1 The year can be evenly divided by 4, is a leap year, unless:
#2 The year can be evenly divided by 100, it is NOT a leap year, unless:
#3 The year is also evenly divisible by 400. Then it is a leap year.
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%400==0 :
        leap = True
    elif year%4 == 0 and year%100 != 0:
        leap = True
    return leap

year = int(input())
print(is_leap(year))