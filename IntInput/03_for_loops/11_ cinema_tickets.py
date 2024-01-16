total_tickets = 0
student_ticket = 0
standard_tickets = 0
kid_tickets = 0
input_line = input()
while input_line != 'Finish':
    movie_name = input_line
    free_seats = int(input())
    counter = 0
    ticket_type = input()
    while ticket_type != "End":
        counter += 1
        total_tickets += 1
        if ticket_type == "student":
            student_ticket += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1
        if counter == free_seats:
            break
        ticket_type = input()
    input_line = input()
    free_seats_to_percent = counter / free_seats * 100
    print(f"{movie_name} - {free_seats_to_percent:.2f}% full.")
print(f"Total tickets: {total_tickets}")
print(f"{student_ticket / total_tickets * 100:.2f}% student tickets.")
print(f"{standard_tickets / total_tickets * 100:.2f}% standard tickets.")
print(f"{kid_tickets / total_tickets * 100:.2f}% kids tickets.")

