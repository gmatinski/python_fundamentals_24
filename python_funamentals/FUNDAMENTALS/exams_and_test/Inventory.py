journal_list = input().split(', ')

command = input().split(' - ')

while command[0] != 'Craft!':
    action = command[0]
    item = command[1]
    if action == "Collect":
        if item not in journal_list:
            journal_list.append(item)
    elif action == "Drop":
        if item in journal_list:
            journal_list.remove(item)
    elif action == "Combine Items":
        old_item, new_item = item.split(':')
        if old_item in journal_list:
            old_item_idx = journal_list.index(old_item)
            journal_list.insert(old_item_idx + 1, new_item)
    elif action == "Renew":
        if item in journal_list:
            journal_list.remove(item)
            journal_list.append(item)
    command = input().split(' - ')
# print(', '.join(journal_list))
print(*journal_list, sep=', ')