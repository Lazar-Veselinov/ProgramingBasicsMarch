book_name = input()
search_input = input()
book_count = 0

while True:
    if search_input == "No More Books":
        print(f"The book you search is not here!\nYou checked {book_count} books.")
        break
    if search_input == book_name:
        print(f"You checked {book_count} books and found it.")
        break

    book_count += 1
    search_input = input()



