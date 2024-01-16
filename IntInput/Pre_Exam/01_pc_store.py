price_cpu_dollars = float(input())
gpu_price_dollars = float(input())
price_dollars_per_ram = float(input())
number_of_rams = int(input())
percent_discount = float(input())

price_cpu_lv = price_cpu_dollars * 1.57
price_gpu_lv = gpu_price_dollars * 1.57
price_ram_lv = price_dollars_per_ram * 1.57
total_ram_lv = price_ram_lv * number_of_rams

price_cpu_lv -= price_cpu_lv * percent_discount
price_gpu_lv -= price_gpu_lv * percent_discount

total_price = price_cpu_lv + price_gpu_lv + total_ram_lv
print(f"Money needed - {total_price:.2f} leva.")