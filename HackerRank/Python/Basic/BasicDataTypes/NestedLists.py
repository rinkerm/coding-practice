if __name__ == '__main__':
    gradebook = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = (name,score)
        gradebook.append(student)
        scores.append(score)
    scores.sort()
    min_v = scores[0]
    runner_up = 0
    for i in range(1,len(scores)):
        if scores[i]>min_v:
            runner_up = scores[i]
            break
    names = [student[0] for student in gradebook if student[1]==runner_up]
    names.sort()
    for name in names:
        print(name)
