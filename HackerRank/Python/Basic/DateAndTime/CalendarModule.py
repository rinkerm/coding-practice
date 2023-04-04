import calendar
line = list(map(int,input().split()))
day = calendar.weekday(line[2],line[0],line[1])
print(calendar.day_name[day].upper())
