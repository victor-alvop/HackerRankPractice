def is_leap(year):
    
    leap = False

    if 1900 <= year <= 10**5:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    else:
        return False

year = int(input('Enter a year: '))
print(is_leap(year))