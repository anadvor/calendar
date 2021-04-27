def isLeap(year):
    if year % 4 != 0:
        vis = False
    else:
        if year % 100 != 0:
            vis = True
        else:
            if year % 400 != 0:
                vis = False
            else:
                vis = True
    return vis


def monlenth(monthNumber, year): # calculates the length of the month
    if monthNumber in (9, 4, 6, 11): # September, April, June, November
        monlen = 30
    elif monthNumber == 2:
        if isLeap(year):
            monlen = 29
        else:
            monlen = 28
    else:
        monlen = 31
    return monlen
    
    
year = int(input("Year: ")) # input year
if isLeap(year):
    print("It's a leap year.")
else:
    print("It's not a leap year.")
monthNumber = int(input("Month Number: "))#input month
if monthNumber < 1 or monthNumber > 12:
    monthNumber = int(input("Try again! Month Number: ")) #re-input if value not correct
day = int(input("Day: ")) #input day
if day < 1 or day > monlenth(monthNumber, year):
    day = int(input("Try again! Day: ")) #re-input if value not correct

d = 25 #current day
m = 4 #current month
y = 2021 #current year
w = 7 # current weekday, 7 for Sunday, 2021.4.25 was Sunday

if year > y: # if input date is later than t=1, else t=-1
    t = 1
elif year == y:
    if monthNumber > m:
        t = 1
    elif monthNumber == m:
        if day > d:
            t = 1
        else:
            t = -1
    else:
        t = -1
else:
    t = -1

while year != y or monthNumber != m or day != d: #if current date != input date
    w += t #change current weekday by 1 up or down
    if w < 1:
        w = 7 #Sunday before Monday
    if w > 7:
        w = 1 #Monday after Sunday
    d += t #change current day
    if d > monlenth(m, y): # if it's January 32nd, February 29th in non-leap year or like that
        d = 1
        m += 1
        if m > 12:
            m = 1
            y += 1
    if d < 1:
        if m == 1: # if it's January 0th
            d = 31
            m = 12
            y -= 1
        else: # if it's zeroth day of other month, not Jan.
            d = monlenth(m-1, y)
            m -= 1
if w == 1:
    print("Monday")
elif w == 2:
    print("Tuesday")
elif w == 3:
    print("Wednesday")
elif w == 4:
    print("Thursday")
elif w == 5:
    print("Friday")
elif w == 6:
    print("Saturday")
else:
    print("Sunday")
