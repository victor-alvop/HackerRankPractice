    if 1900 <= year and year <= 10 **5:
        if year % 4 == 0:
            print(year % 4)
            if year % 100 == 0:
                if year % 400 == 0:
                    leap = True
                else:
                    leap = False
            else:
                leap = True