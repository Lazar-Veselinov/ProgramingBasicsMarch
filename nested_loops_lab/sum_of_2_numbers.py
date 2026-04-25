int_begin = int(input())
int_end = int(input())
magic_number = int(input())

count_combination = 0
magic_number_found = False

for i in range(int_begin, int_end + 1):
    for j in range(int_begin, int_end + 1):
        count_combination += 1
        if i + j == magic_number:
            magic_number_found = True
            print(f"Combination N:{count_combination} "
                  f"({i} + {j} = "
                  f"{magic_number})")
            break
    if magic_number_found:
        break

if not magic_number_found:
    print(f"{count_combination} "
          f"combinations - neither equals {magic_number}")