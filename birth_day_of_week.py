import datetime
import calendar

weekdays =['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Satuday', 'Sunday']

def split_date(birthday):
    year, month, day = birthday.split('-')
    return year, month, day

def get_birthday(birthday):
    year, month, day = split_date(birthday)
    bdate = datetime.datetime(int(year), int(month), int(day))
    weekday = bdate.weekday()
    day = weekdays[weekday]
    return day

def listToString(x):
    String = " "
    return (String.join(x))

def main():
    birthdate = '2086-01-11'
    dates = get_birthday(birthdate)
    print('You were born on ',dates)
    
main()