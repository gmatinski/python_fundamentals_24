bad_grades_allowed = int(input())

bad_attempts = 0
take_a_break = False
grade_overall = 0
number_of_grade = 0
name_of_last = ""

name_of_exc = input()
while name_of_exc != "Enough":
    grade = int(input())
    number_of_grade += 1
    grade_overall += grade
    if grade <= 4:
        bad_attempts += 1
    if bad_attempts >= bad_grades_allowed:
        take_a_break = True
        break
    name_of_exc = input()
    if name_of_exc != "Enough":
        name_of_last = name_of_exc

if take_a_break:
    print(f"You need a break, {bad_attempts} poor grades.")
else:
    print(f"Average score: {grade_overall / number_of_grade:.2f}\nNumber of problems: {number_of_grade}\n"
          f"Last problem: {name_of_last}")