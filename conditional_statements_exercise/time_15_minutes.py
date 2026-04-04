hours = int(input())
minutes = int(input())

hours_in_minutes = hours * 60
total_minutes = hours_in_minutes + minutes
total_minutes_plus_15 = total_minutes + 15

hour = total_minutes_plus_15 // 60
minutes1 = total_minutes_plus_15 % 60

if hour >= 24:
    hour = hour - 24

if minutes1 < 10:
    print(f"{hour}:0{minutes1}")
else:
    print(f"{hour}:{minutes1}")
