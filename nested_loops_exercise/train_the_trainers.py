judges = int(input())

total_grade_sum = 0
count_presentation = 0

while True:
    presentation = input()

    if presentation == "Finish":
        print(f"Student's final assessment is {total_grade_sum / count_presentation:.2f}.")
        break

    current_grade_sum = 0
    count_presentation += 1

    for n in range(judges):
        grade = float(input())
        current_grade_sum += grade

    current_average_grade = current_grade_sum / judges
    total_grade_sum += current_average_grade

    print(f"{presentation} - {current_average_grade:.2f}.")