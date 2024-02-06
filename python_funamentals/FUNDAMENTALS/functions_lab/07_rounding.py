numbers = input().split()

int_nums = [float(number) for number in numbers]
new_list = []
for index in int_nums:
    absolute = round(index)
    new_list.append(absolute)

print(new_list)
#
# # def process_numbers(input_numbers):
# #     float_nums = [float(number) for number in input_numbers]
# #     new_list = []
# #     for num in float_nums:
# #         absolute = round(abs(num))
# #         new_list.append(absolute)
# #     return new_list
# #
# # # Example usage:
# # numbers = input().split()
# # result = process_numbers(numbers)
# # print(result)
