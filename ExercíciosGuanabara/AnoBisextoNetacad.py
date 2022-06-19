def is_year_leap(year):
#
# Your code from LAB 4.3.1.6.
#
    if year % 400 == 0:
        return True
    else:
        if year % 4 == 0 and year % 100 != 0:
            return True
        else:
            return False


def days_in_month(year, month):
#
# Your code from LAB 4.3.1.7.
#
    mes31 = [1,3,5,7,8,10,12]
    mes30 = [4,6,9,11]
    
    if month == 2:
        if is_year_leap(year) == True:
            return 29
        else:
            return 28
    else:
        if month > 12 or month < 1:
            return None
        elif month in (mes31):
            return 31
        else:
            return 30

def day_of_year(year, month, day):
#
# Write your new code here.
#
    
    if day > days_in_month(year, month) or day < 1:
        return None
    else:
        return year, month, day

print(day_of_year(2001, 4, 31))
