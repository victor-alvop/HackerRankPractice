n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()

decimal_number = round(sum(student_marks.get(query_name))/len(student_marks.get(query_name)),2)
print(f"{decimal_number:.2f}")