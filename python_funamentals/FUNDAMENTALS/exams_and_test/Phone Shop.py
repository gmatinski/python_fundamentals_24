list_of_phones = input().split(', ')
command = input().split(" - ")

while True:
    if command[0] == "End":
        break

    task = command[0]
    phone = command[1]

    if task == "Add":
        if phone not in list_of_phones:
            list_of_phones.append(phone)

    elif task == "Remove":
        if phone in list_of_phones:
            list_of_phones.remove(phone)

    elif task == "Bonus phone":
        old_phone, new_phone = phone.split(":")
        if old_phone in list_of_phones:
            old_phone_idx = list_of_phones.index(old_phone)
            list_of_phones.insert(old_phone_idx + 1, new_phone)
    elif task == "Last":
        if phone in list_of_phones:
            list_of_phones.remove(phone)
            list_of_phones.append(phone)

    command = input().split(" - ")
print(*list_of_phones, sep=", ")
