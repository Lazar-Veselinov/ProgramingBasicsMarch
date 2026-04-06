exam_hour = int(input())
exam_minutes = int(input())
arr_hour = int(input())
arr_minutes = int(input())

exam_min = exam_hour * 60 + exam_minutes
arr_min = arr_hour * 60 + arr_minutes

state = ""

if exam_min < arr_min:
    state = "Late"
elif exam_min - 30 <= arr_min <= exam_min:
    state = "On time"
else:
    state = "Early"

print(f"{state}")

time_difference = abs(arr_min - exam_min)
diff_hour = time_difference // 60
diff_minute = time_difference % 60

if arr_min != exam_min:
    if exam_min - 60 < arr_min < exam_min:
        print(f"{time_difference} minutes before the start")
    elif arr_min <= exam_min - 60:
        if diff_minute < 10:
            print(f"{diff_hour}:0{diff_minute} hours before the start")
        else:
            print(f"{diff_hour}:{diff_minute} hours before the start")
    elif exam_min < arr_min < exam_min + 60 :
        print(f"{time_difference} minutes after the start")
    elif exam_min + 60 <= arr_min:
        if diff_minute < 10:
            print(f"{diff_hour}:0{diff_minute} hours after the start")
        else:
            print(f"{diff_hour}:{diff_minute} hours after the start")