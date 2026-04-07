name = input()

count_fail = 0
count_year = 1
sum_grades = 0

while True:
    grade = float(input())

    if grade < 4.00:
        count_fail += 1
        if count_fail > 1:
            passed = False
            print(f"{name} has been excluded at {count_year} grade")
            break
        continue

    sum_grades += grade
    if count_year == 12:
        avg_score = sum_grades / 12
        print(f"{name} graduated. Average grade: {avg_score:.2f}")
        break
    count_year += 1