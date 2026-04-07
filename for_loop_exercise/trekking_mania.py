num_groups = int(input())

people_musala = 0
people_monblan = 0
people_kilimanjaro = 0
people_k2 = 0
people_everest = 0

total_num_people = 0
for _ in range(num_groups):
    numb_people_in_group = int(input())

    total_num_people += numb_people_in_group

    if numb_people_in_group <= 5:
        people_musala += numb_people_in_group
    elif 6 <= numb_people_in_group <= 12:
        people_monblan += numb_people_in_group
    elif 13 <= numb_people_in_group <= 25:
        people_kilimanjaro += numb_people_in_group
    elif 26 <= numb_people_in_group <= 40:
        people_k2 += numb_people_in_group
    else:
        people_everest += numb_people_in_group

percent_musala = (people_musala / total_num_people) * 100
percent_monblan = (people_monblan / total_num_people) * 100
percent_kilimanjaro = (people_kilimanjaro / total_num_people) * 100
percent_k2 = (people_k2 / total_num_people) * 100
percent_everest = (people_everest / total_num_people) * 100

print(f"{percent_musala:.2f}%\n{percent_monblan:.2f}%\n{percent_kilimanjaro:.2f}%\n{percent_k2:.2f}%\n{percent_everest:.2f}%")