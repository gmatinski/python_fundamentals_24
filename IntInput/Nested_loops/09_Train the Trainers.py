number_of_judges = int(input())
name_of_presentation = input()
total_grade = 0
avg_grade = 0
absolute = 0
judge_total = 0

while name_of_presentation != "Finish":
    for i in range(1, number_of_judges +1):
        grade = float(input())
        total_grade += grade
        absolute += grade
    avg_grade = total_grade / number_of_judges
    total_grade = 0
    judge_total += number_of_judges
    print(f"{name_of_presentation} - {avg_grade:.2f}.")
    name_of_presentation = input()
absolute = absolute / judge_total
print(f"Student's final assessment is {absolute:.2f}.")
