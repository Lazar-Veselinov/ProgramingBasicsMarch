num_visitors = int(input())

num_back_trainers = 0
num_chest_trainers = 0
num_legs_trainers = 0
num_abs_trainers = 0
num_protein_shakes = 0
num_protein_bars = 0
num_protein = 0

num_working_out = 0
for n in range(num_visitors):
    activity = input()

    if activity == "Back":
        num_working_out += 1
        num_back_trainers += 1
    elif activity == "Chest":
        num_working_out += 1
        num_chest_trainers += 1
    elif activity == "Legs":
        num_working_out += 1
        num_legs_trainers += 1
    elif activity == "Abs":
        num_working_out += 1
        num_abs_trainers += 1
    elif activity == "Protein shake":
        num_protein += 1
        num_protein_shakes += 1
    elif activity == "Protein bar":
        num_protein += 1
        num_protein_bars += 1

percent_working_out = num_working_out / num_visitors * 100
percent_protein_shake = num_protein / num_visitors * 100

print(f"{num_back_trainers} - back\n"
      f"{num_chest_trainers} - chest\n"
      f"{num_legs_trainers} - legs\n"
      f"{num_abs_trainers} - abs\n"
      f"{num_protein_shakes} - protein shake\n"
      f"{num_protein_bars} - protein bar\n"
      f"{percent_working_out:.2f}% - work out\n"
      f"{percent_protein_shake:.2f}% - protein")