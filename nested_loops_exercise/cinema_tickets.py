total_tickets = 0

percent_student = 0
percent_standard = 0
percent_kid = 0

count_student = 0
count_standard = 0
count_kid = 0

while True:
    movie = input()
    free_spaces = int(input())

    current_movie_tickets = 0

    if movie == 'Finish':
        percent_student = count_student * 100 / total_tickets
        percent_standard = count_standard * 100 / total_tickets
        percent_kid = count_kid * 100 / total_tickets

        print(f"Total tickets: {total_tickets}\n"
              f"{percent_student}% student tickets.\n"
              f"{percent_standard}% standard tickets.\n"
              f"{percent_kid}% kids tickets.")
        break

    percent_filled = 0

    while current_movie_tickets < free_spaces:
        command = input()

        if command == 'End':
            break

        if command == "student":
            count_student += 1
            total_tickets += 1
            current_movie_tickets += 1

        elif command == "standard":
            count_standard += 1
            total_tickets += 1
            current_movie_tickets += 1

        elif command == "kid":
            count_kid += 1
            total_tickets += 1
            current_movie_tickets += 1

    percent_filled = total_tickets / (free_spaces + total_tickets) * 100

    print(f"{movie} - {percent_filled}% full.")
