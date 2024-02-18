wagons = [0] * int(input())  # * 3 = [0,0,0]
while True:
    command = input().split()
    if command[0] == "End":
        print(wagons)
        break
    elif command[0] == "add":
        number_of_ppl = int(command[1])
        wagons[-1] += number_of_ppl
    elif command[0] == "insert":
        index = int(command[1])
        number_of_ppl = int(command[2])
        wagons[index] += number_of_ppl
    elif command[0] == "leave":
        index = int(command[1])
        number_of_ppl = int(command[2])
        wagons[index] -= number_of_ppl
