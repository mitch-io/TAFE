commonMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leapYearMonths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def dayNumber(year, month, day):
    assert 0 < year < 3000, "year is incorrect"
    assert 0 < month < 13, "month is incorrect"
    assert 0 < day < 32, "day is incorrect"
    if isLeap(year) == True:
        return(sum(leapYearMonths[:month-1]) + day)
    else:
        return(sum(commonMonths[:month-1]) + day)

def isLeap(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0:
        if year % 100 == 0:
            return False
        return True
    else:
        return False

try:
    print(dayNumber(2020, 1, 15))
except

