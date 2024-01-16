cake_length = int(input())
cake_width = int(input())

pieces = cake_width * cake_length
while pieces > 0:
    one_piece = input()
    if one_piece.isdigit():
        one_piece = int(one_piece)
        pieces -= one_piece
    if pieces <= 0:
        print(f"No more cake left! You need {abs(pieces)} pieces more.")
        break
    if one_piece == "STOP":
        print(f"{pieces} pieces are left.")
        break
