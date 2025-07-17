n = int(input())
students = []

for _ in range(n):
    name = input()
    score = float(input())
    students.append([name, score])

scores = [score for name, score in students]
unique_scores = sorted(set(scores))
second_lowest = unique_scores[1]

second_lowest_students = [name for name, score in students if score == second_lowest]
second_lowest_students.sort()


for name in second_lowest_students:
    print(name)
