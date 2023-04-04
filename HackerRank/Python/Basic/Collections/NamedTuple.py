from collections import namedtuple
n = int(input())
Student=namedtuple('Student',input().split())
marks = [int(Student(*input().split()).MARKS) for i in range(0,n)]
print(sum(marks)/len(marks))
