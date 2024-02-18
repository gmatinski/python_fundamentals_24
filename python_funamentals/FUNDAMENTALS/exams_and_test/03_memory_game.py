element_seq = input().split()

command = input().split()
moves = 0

while True:
    if command[0] == "end":
        break
    idx_one = int(command[0])
    idx_two = int(command[1])
    moves += 1

    if 0 <= idx_one < len(element_seq) and 0 <= idx_two < len(element_seq):
        if element_seq[idx_one] == element_seq[idx_two]:
            # Remove elements at the specified indices if they are equal
            matching_element = element_seq.pop(max(idx_one, idx_two))
            element_seq.pop(min(idx_one, idx_two))
            print(f'Congrats! You have found matching elements - {matching_element}!')
        else:
            print("Try again!")
    else:
        middle_index = len(element_seq) // 2
        new_el1 = f'-{moves}a'
        new_el2 = f'-{moves}a'
        element_seq.insert(middle_index, new_el1)
        element_seq.insert(middle_index, new_el2)
        print("Invalid input! Adding additional elements to the board")
    if not element_seq:
        print(f'You have won in {moves} turns!')
        break

    command = input().split()
if element_seq:
    print(f'Sorry you lose :(\n{" ".join(element_seq)}')