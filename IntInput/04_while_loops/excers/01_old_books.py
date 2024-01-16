searched_book = input()
boolean = False
counter_books = 0

current_book = input()
while current_book != "No More Books":
    if current_book != searched_book:
        counter_books += 1
    if current_book == searched_book:
        boolean = True
        break
    current_book = input()
if boolean:
    print(f"You checked {counter_books} books and found it.")
if not boolean:
    print(f"The book you search is not here!")
    print(f"You checked {counter_books} books.")