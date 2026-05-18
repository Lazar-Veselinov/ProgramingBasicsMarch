player_name = input()
total_points = 301
shots = 0
unsuccessful_shots = 0

while total_points > 0:
    command = input()

    if command == "Retire":
        print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")
        break

    points = int(input())

    if command == "Single":
        score = points
    elif command == "Double":
        score = points * 2
    elif command == "Triple":
        score = points * 3

    if score > total_points:
        unsuccessful_shots += 1
        continue

    shots += 1

    total_points -= score

else:
    print(f"{player_name} won the leg with {shots} shots.")