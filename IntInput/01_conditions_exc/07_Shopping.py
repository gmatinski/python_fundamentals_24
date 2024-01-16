budget = float(input())
num_of_gpu = int(input())
num_of_cpu = int(input())
num_of_ram = int(input())
gpu_price = 250 * num_of_gpu

cpu_price = (gpu_price * 0.35) * num_of_cpu
ram_price = (gpu_price * 0.10) * num_of_ram
total = gpu_price + cpu_price + ram_price
if num_of_gpu > num_of_cpu:
    total = total * 0.85

if budget >= total:
    print(f"You have {budget - total:.2f} leva left!")
else:
    print(f"Not enough money! You need {total - budget:.2f} leva more!")
