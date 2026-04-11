low_grades = int(input())

avg_score = 0
sum_scores = 0
scores_count = 0
low_grades_count = 0
last_exercise = ""

while True:
    exercise_name = input()

    if exercise_name == "Enough":
        avg_score = sum_scores / scores_count
        print(f"Average score: {avg_score:.2f}\nNumber of problems: {scores_count}\nLast problem: {last_exercise}")
        break

    score = int(input())
    scores_count += 1
    sum_scores += score

    if score <= 4:
        low_grades_count += 1
        if low_grades_count >= low_grades:
            print(f"You need a break, {low_grades_count} poor grades.")
            break

    last_exercise = exercise_name
