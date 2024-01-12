n = int(input())

grading_book = {}

for i in range(n):
    name, fl_grade = input().split(" ")
    grade = float(fl_grade)

    if name in grading_book.keys():
        grading_book[name].append(grade)
    else:
        grading_book[name] = [grade]

for name, grades in grading_book.items():
    avg = sum(grades) / len(grades)
    formatted = f"{' '.join([f'{g:.2f}' for g in grades])}"
    print(f"{name} -> {formatted} (avg: {avg:.2f})")

