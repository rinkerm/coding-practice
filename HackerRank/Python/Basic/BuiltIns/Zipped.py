args = list(map(int,input().split()))
scores = []
for i in range(0,args[1]):
    scores.append(list(map(float,input().split())))
student_scores = list(zip(*scores))
for j in range(0,args[0]):
    print(sum(student_scores[j])/len(student_scores[j]))
