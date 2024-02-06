def perfect_num(num):
    sum_prefect = 0
    for divisor in range(1,num):
        if num % divisor == 0:
            sum_prefect+=divisor
    if sum_prefect == num:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(perfect_num(number))