import math
ab = int(input())
bc = int(input())
mcb = math.degrees(math.atan(ab/bc))
mcb = round(mcb)
print(mcb,chr(176),sep='')
