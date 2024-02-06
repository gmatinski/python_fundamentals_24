deck_cards = input().split()            # ['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h']
suffle_count = int(input())
for shuffle in range(suffle_count):
    middle_of_deck = len(deck_cards) // 2
    left_part = deck_cards[:middle_of_deck]
    right_part = deck_cards[middle_of_deck:]
    new_deck = []
    for card_index in range(len(left_part)):
        new_deck.append(left_part[card_index])
        new_deck.append(right_part[card_index])
        deck_cards = new_deck
print(deck_cards)
